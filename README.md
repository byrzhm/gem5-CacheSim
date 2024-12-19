# CacheSim

## Instructions

First, build gem5 from source. The [building gem5](https://www.gem5.org/documentation/general_docs/building)
provides more details on building gem5 and its dependencies.


```bash
git clone https://github.com/byrzhm/gem5-CacheSim.git --recursive
cd gem5-CacheSim
docker pull ghcr.io/gem5/ubuntu-20.04_all-dependencies:v24-0
docker run -u $UID:$GID --volume ./:/gem5-CacheSim --rm -it ghcr.io/gem5/ubuntu-20.04_all-dependencies:v24-0
# Now in docker
cd /gem5-CacheSim/gem5
scons build/X86/gem5.opt -j`nproc`
```

Now run gem5 in docker.

```bash
./build/X86/gem5.opt ./configs/learning_gem5/part1/simple.py
```

## Related Resources

- [gem5 github repo](https://github.com/gem5/gem5)
- [erwanregy/Cache-Simulation](https://github.com/erwanregy/Cache-Simulation)
- [gem5 101](https://www.gem5.org/documentation/learning_gem5/gem5_101/)
- [gem5 hpca 2024](https://www.gem5.org/assets/files/hpca2024-tutorial/gem5-tutorial-hpca-2024-slides.pdf)
- [getting started with gem5](https://www.gem5.org/getting_started/)
