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
│   │── icon.png
├── src
│   └── extension.py
├── demos
│   └── Example_with_Python_node.knwf
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
3. _(Optional)_ Modify the `src/extension.py` file to implement your own logic.
4. _(Optional)_ Add python packages to the environment with the following command, or by manually editing the `pixi.toml` file:

    ```bash
    pixi add <package_name>
    ```

    It is good practice to keep the `pixi.lock` file in this repository and commit the changes to it whenever you add packages or update them with `pixi update`.
5. **Install** the python environment:
    ```bash
    pixi install
    ```
6. **Test** the extension in the KNIME Analytics Platform with the extension in debug mode by adding the following line to the knime.ini file (adjust <path_to_this_repository> in the config.yml):    
    ```
    -Dknime.python.extension.config=<path/to/your/config.yml>
    ```
   This will start the KNIME Analytics Platform with your extension installed. You can now test your extension in the KNIME Analytics Platform (e.g. demo workflow). 
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
9. To **publish** on KNIME Hub, follow the [KNIME Hub documentation](https://docs.knime.com/latest/knime_hub_guide/index.html#publishing_your_extension).

For detailed instructions on how to create a KNIME Python extension, please refer to the [KNIME Python Extension documentation](https://docs.knime.com/latest/pure_python_node_extensions_guide/index.html).

## Join the Community

* [KNIME Forum](https://forum.knime.com)