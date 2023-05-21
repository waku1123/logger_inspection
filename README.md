# logger_inspection
pythonのロガーについての試行錯誤

## ロガー設定ファイル
状況に応じて、yaml/jsonのいずれかを使用する。
- [yaml](./config/logger_conf.yaml)
 
  ファイルのloadに`PyYaml`が必要
  ```shell
  $ pip install PyYaml
  ```
- [json](./config/logger_conf.json)

  デフォルトでload可能

## loggerについて

- 細かく設定したい場合は`loggers`に定義し、スクリプトで`getLogger(<name>)`して使用する。
- rootロガーを使用する場合は`getLogger(__file__)`して使用する。

- 標準出力、ファイル出力の有無については、各ロガーの`handlers`で設定する
