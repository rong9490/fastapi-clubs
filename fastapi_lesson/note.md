```
  哔哩哔哩课程Fastapi: https://www.bilibili.com/video/BV1eKpizeEnb
  10月1日
```

```
  Anaconda 命令行工具 / install, uninstall (跨语言依赖, 开箱即用) -> anaconda.org -> channel -> miniconda / conda-forge
  -c channel / defaults / 修改配置文件 / miniforge源指向 / 依赖求解 / mamba(c++版) /

  包依赖管理 pip + venv / conda / mamba / uv /
  conda -V # 24.7.1
  conda update
  创建虚拟环境: conda create -n fastapi_env python=3.12
  激活虚拟环境: conda activate fastapi_env
  退出虚拟环境: conda deactivate

  Channels:
  - defaults
  Platform: osx-arm64
  Collecting package metadata (repodata.json): done
  Solving environment: done

  ## Package Plan ##
  environment location: /opt/anaconda3/envs/fastapi_env
  added / updated specs:
    - python=3.12
  The following packages will be downloaded:
```

```
  安装依赖
  pip install fastapi[standard]
  pip install fastapi==0.115.12
  pip install uvicoron==0.34.2

```
