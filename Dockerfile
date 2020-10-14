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
RUN julia -e 'import Pkg; Pkg.add(url="https://github.com/coudertlab/CrystalNets.jl")'
RUN export JULIAPACKAGE=$(julia -e 'using CrystalNets; println(pathof(CrystalNets))')

RUN useradd cheminfo

WORKDIR /home/cheminfo

COPY requirements.txt .

COPY crystal_analysis_webservice ./crystal_analysis_webservice

COPY README.md .

RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn -w 4 crystal_analysis_webservice.crystal_analysis_webservice:app -b 0.0.0.0:$PORT -k uvicorn.workers.UvicornWorker