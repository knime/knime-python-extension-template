# ![Image](https://www.knime.com/sites/default/files/knime_logo_github_40x40_4layers.png) KNIME® -  KNIME PYTHON EXTENSION TEMPLATE

[![CI](https://github.com/knime/knime-python-extension-template/actions/workflows/ci.yml/badge.svg)](https://github.com/knime/knime-python-extension-template/actions/workflows/ci.yml) [![Code Quality Check](https://github.com/knime/knime-python-extension-template/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/knime/knime-python-extension-template/actions/workflows/code-quality-check.yml)
[![Extension Bundling](https://github.com/knime/knime-python-extension-template/actions/workflows/bundle-extension.yml/badge.svg)](https://github.com/knime/knime-python-extension-template/actions/workflows/bundle-extension.yml)

This repository is maintained by the [KNIME Team Rakete](mailto:team-rakete@knime.com).

It provides a template for creating KNIME Python extensions.

## Contents

This repository contains a template KNIME Python Extensions.
The code is organized as follows:

```
.
├── icons
│   └── icon.png
├── src
│   ├── __init__.py
│   └── extension.py
├── demo
│   └── Example_with_Python_node.knwf
├── tests
│   ├── conftest.py
│   └── test_extension.py
├── knime.yml
├── pixi.toml
├── config.yml
│── LICENSE.TXT
└── README.md
```

## Instructions

You can find instructions on how to work with our code or develop python extensions for KNIME Analytics Platform in the KNIME documentation:
* [KNIME Python Extension](https://docs.knime.com/latest/pure_python_node_extensions_guide/index.html)

## Minimal Instructions to create a KNIME Python extension
### Prerequisites:
* [KNIME Analytics Platform](https://www.knime.com/downloads/overview)
* [git](https://git-scm.com/downloads)
* [pixi](https://pixi.sh/latest/)

### Instructions:
1. **Clone** this repository or use it as a **template** (click on the green "Use this template" button):
2. **Edit** `knime.yml` -  provide your metadata, license, ...
3. **Modify** the `src/extension.py` file or **add** further files to implement your own logic. Note that every py file equivalent to one node needs to be imported in the init.py file.
4. **Install** the python environment:
    ```bash
    pixi install
    ```
    This will install the Python environment as defined in the `pixi.toml` file. If you leave this file unchanged, the Python environment that is installed will have the needed KNIME packages installed per default (knime-python-versions). 
5. _(Optional)_ Add python packages to the environment with the following command, or by manually editing the `pixi.toml` file:
    ```bash
    pixi add <package_name>
    ```
    Note that you have to run the `pixi install` command again after manually editing the `pixi.toml` file. 
6. **Install** the extension in debug mode in your KNIME Analytics Platform by running the following command: 
    ```
    pixi run register-debug-in-knime
    ```
   Previously this step required modifying the `config.yml`and `knime.ini` files manually. This improvement will allow you to select your KNIME Analytics Platform installation and append the `-Dknime.python.extension.debug_knime_yaml_list=<path/to/your/knime.yml>` argument automatically to the according `knime.ini` file. You can now test your extension in the KNIME Analytics Platform (e.g. demo workflow). 
7. **Bundle** your extension:
    ```bash
    pixi run build
    ```
    or if you want the extension's local update site in a specific location (default is `./local_update_site`):
    ```bash	
    pixi run build dest=<path_to_your_update_site>
    ```
8. **Install** the update site in KNIME via
    ```bash
    File > Install KNIME Extensions... > Available Software Sites > Add... 
    ```
    and enter the path to your update site (by default `./local_update_site`). After that, you can install your extension.
9. To **publish** on KNIME Hub, follow the [KNIME Hub documentation](https://docs.knime.com/latest/development_contribute_extension/index.html#_publish_your_extension).

For detailed instructions on how to create a KNIME Python extension, please refer to the [KNIME Python Extension documentation](https://docs.knime.com/latest/pure_python_node_extensions_guide/index.html).

## Join the Community

* [KNIME Forum](https://forum.knime.com)