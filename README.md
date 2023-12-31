# startstop_lambda

EC2起動・停止するLambda

## デプロイ実施

~~~python
poetry run python deploy.py
~~~

## ローカルテストの方法

TODO pathがあわずImportErrorが発生するので、適切な対応策を探すべき

環境変数を設定する。

~~~zsh
export AWS_DEFAULT_REGION=ap-northeast-1
export LOG_LEVEL=INFO
export POWERTOOLS_SERVICE_NAME=local_test
~~~

以下のpytestコマンドを実行する。

~~~python
poetry run pytest -s ec2startstop/tests/unit/test_ec2start.py
poetry run pytest -s ec2startstop/tests/unit/test_ec2stop.py
~~~

## 開発時のTIPS

開発用のパッケージを使いする場合は、以下コマンドを使用する。

~~~zsh
poetry add aws-sam-cli --group dev
~~~

## 参考文献

- [re:Post](https://repost.aws/ja/knowledge-center/start-stop-lambda-eventbridge)
- [subprocess](https://techblog.asahi-net.co.jp/entry/2023/10/11/151441)