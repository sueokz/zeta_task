# zeta_task
zetachain(ブロックチェーンのL2)の送金等を自動化するためのコード。

# 公開の予定
なし

# 工夫した点
これまでAPI・秘密鍵や細かな変数も直に書いてきたが、セキュリティや可読性を意識してconfig.py・abi.pyに分けた。  
環境によって推奨コードが異なることやエラーが起きやすいと感じたのでどの環境でも書けるようにrequirement.txtを作成した。

# 改善
手数料改善のためにやり方を変更。　5/30
サーバーレスで定期実行するように変更。　6/1
→AWS LAMBDAだと、環境構築でweb3と相性悪い
Cloud functionを採用

# 課題
定期実行→AWS LAMBDAで実装。→Cloud functionで解決 6/1

# UPDATE
5/30
6/1
