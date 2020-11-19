FROM python:3.8-slim-buster

COPY install_packages.sh .
RUN ./install_packages.sh

# Install Julia and the package 
ENV JULIA_DEPOT_PATH=/opt/julia
ENV JULIA_PKGDIR=/opt/julia
ENV JULIA_VERSION=1.5.2

WORKDIR /tmp
RUN mkdir "/opt/julia-${JULIA_VERSION}" && \
    wget -q https://julialang-s3.julialang.org/bin/linux/x64/$(echo "${JULIA_VERSION}" | cut -d. -f 1,2)"/julia-${JULIA_VERSION}-linux-x86_64.tar.gz" && \
    tar xzf "julia-${JULIA_VERSION}-linux-x86_64.tar.gz" -C "/opt/julia-${JULIA_VERSION}" --strip-components=1 && \
    rm "/tmp/julia-${JULIA_VERSION}-linux-x86_64.tar.gz"
RUN ln -fs /opt/julia-*/bin/julia /usr/local/bin/julia
RUN julia -e 'import Pkg; Pkg.add(url="https://github.com/kjappelbaum/CrystalNets.jl")'
RUN useradd cheminfo

COPY entrypoint.sh /

WORKDIR /home/cheminfo

COPY requirements.txt .
COPY logging_config.ini .

COPY crystal_analysis_webservice ./crystal_analysis_webservice

COPY README.md .


RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/entrypoint.sh"]

CMD uvicorn crystal_analysis_webservice.crystal_analysis_webservice:app --host=0.0.0.0 --port=$PORT --workers=$WORKERS --loop="uvloop" --http="httptools" --log-config=logging_config.ini --limit-concurrency=$CONCURRENCY_LIMIT