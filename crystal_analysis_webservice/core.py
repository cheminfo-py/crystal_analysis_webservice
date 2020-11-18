import subprocess
import os
import tempfile
import contextlib
from func_timeout import func_set_timeout

JULIAPACKAGE = os.getenv("JULIAPACKAGE")
PROJECTPATH = str(os.path.abspath(os.path.join(JULIAPACKAGE, "../..")))

JULIA_EXEC_COMMAND = "julia -p 1 --project={PROJECTPATH} {JULIAPACKAGE} -c auto {file}"
from . import __version__


@contextlib.contextmanager
def temporary_filename(suffix=None):
    """Context that introduces a temporary file.

  Creates a temporary file, yields its name, and upon context exit, deletes it.
  (In contrast, tempfile.NamedTemporaryFile() provides a 'file' object and
  deletes the file as soon as that file object is closed, so the temporary file
  cannot be safely re-opened by another library or process.)

  Args:
    suffix: desired filename extension (e.g. '.mp4').

  Yields:
    The name of the temporary file.
  """
    import tempfile

    try:
        f = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
        tmp_name = f.name
        f.close()
        yield tmp_name
    finally:
        os.unlink(tmp_name)


@func_set_timeout(300)
def run_topology_analysis(fileContent: str, extension: str = "cif"):
    out = ""
    with temporary_filename("." + extension) as filename:
        with open(filename, "w") as fh:
            fh.write(fileContent)
        process = subprocess.Popen(
            JULIA_EXEC_COMMAND.format(
                JULIAPACKAGE=JULIAPACKAGE, PROJECTPATH=PROJECTPATH, file=filename
            ),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out_, err = process.communicate()
    if out_:
        try:
            out_ = out_.decode("ascii")
            out_ = out_.split("\n")
            if "ERROR" in out:
                errorline = None
                for line in out_:
                    if "ERROR" in line:
                        errorline = line

                raise ValueError(errorline)
            if out_:
                if len(out_) > 2:
                    out = out_[-2]
                    os.unlink(out_[0].split()[-1])
                else:
                    out = out_[0]

            else:
                raise ValueError

        except Exception as e:
            raise ValueError("Some error occured {}".format(e)) from e

    return {
        "rcsrName": out,
        "apiVersion": __version__,
        "rcsrLink": f"http://rcsr.anu.edu.au/nets/{out}",
    }

