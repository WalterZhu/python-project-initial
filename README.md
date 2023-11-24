# 一个自用基本 Python 项目脚手架

本项目是一个轻量实用的 Python 项目脚手架，集成了简单的日志，配置文件管理，处理了 python 脚本间的依赖关系，避免重复导入等问题。适用于各种 Python 项目（例如数据科学，web 服务器等）。

# 功能

- 依赖管理：使用 poetry 管理项目依赖
- 日志管理：统一化日志格式，分别输出到 stdout 和 .log/app.log
- 配置文件管理：根据不同环境加载不同配置文件。
- 测试管理：使用 pytest 管理测试用例

# 使用方法

## 1 安装 poetry 依赖管理器：

macOS, Linux, Windows(WSL)：
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

其他平台的 poetry 安装方式见：[Introduction | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/#installing-with-the-official-installer)

## 2 clone 本项目到本地

```bash
git clone git@github.com
```

## 3 （可选）替换 poetry 的 python 版本

项目默认 3.11 版本，如果你想使用其他版本，可：
打开 `pyproject.toml` ，将 `python = "^3.11"` 替换为你想要的 python 版本

## 4 切换到项目根目录下，安装依赖

```bash
poetry install
```

## 5 IDE设置

## 6 添加项目变量

项目变量文件为.env
```bash
cp .env.example .env
```

## 7 项目目录

- 代码可以放在 `src` 目录下。
- 测试用例放在 `test` 目录下。

### 7.1 引入自己写的模块

引入自己编写的模块时，使用 `src` 作为根目录起始的路径，如：
```python
# 例如，在 src/service 目录下写了一个 demo_service.py 文件，在其他文件中引入
# 引入的文件路径不写 src，直接从 service 开始即可
from server.demo_service import foo
```

### 7.2 在代码中引入项目变量

在 `.env` 中增加配置

```env
foo = 'bar'
```

可在代码中使用以下方式引入，中的层级用字符串列表表示：

```python
# 引入 ConfigManager
from component.ConfigManager import config_manager

# 获取 yaml 中配置的变量 foo.bar
try:
    config_str = config_manager.get_value(['foo', 'bar'])
    # > test_paramter
    print(config_str)
except KeyError:
    # 如未找到该变量，抛出 KeyError 异常
    print('foo.bar 不存在')
```

### 7.3 使用日志

在代码中引入日志：

```python
from logger import logger

# 输出日志
logger.debug('debug log')
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
```

logger stdout，warning 和 error level 的日志将输出到 stderr。


## 8 运行

程序将按照顺序指定运行环境：
1. 命令行实参：如 `poetry run main`

## 9 写测试

测试文件统一放在 test 目录下，文件名以 `test_` 开头，如 `test_main.py`

## 10 安装依赖

直接用 poetry 安装，会自动修改 `pyproject.toml` 文件

```bash
poetry add <package-name>
poetry install
```

## 11 修改日志打印到控制台的输出 Level

在 .env 文件夹中配置各个环境的日志输出等级
```bash
# 配置为 INFO 级别
LOG_LEVEL=INFO  # 支持 DEBUG, INFO, WARNING, ERROR, CRITICAL 不同等级
```