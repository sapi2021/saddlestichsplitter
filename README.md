# saddlestichsplitter

## 目的

中綴じ製本の冊子を電子化した際にページ番号がばらばらになって読みにくい。
その問題の解消のために PDF を分割して、リオーダーするためのスクリプト

* 元の PDF の状態
```
  1枚目                               2枚目                              3枚目
  ---------------------------------  ---------------------------------  ---------------------------------     
  |               |               |  |               |               |  |               |               |    
  |               |               |  |               |               |  |               |               |  
  | 表表紙         |背表紙          |  | Page20        |Page1          |  | Page20        |Page1          |  
  |               |               |  |               |               |  |               |               |  
  |               |               |  |               |               |  |               |               |     
  ---------------------------------  ---------------------------------  ---------------------------------      
```
* 加工後の PDF の状態
```
  1枚目               2枚目                                    21枚目             22枚目                        
  -----------------  ----------------                        -----------------  ----------------
  |               |  |              |                        |               |  |              |
  |               |  |              |                        |               |  |              |
  | 表表紙         |  |Page1         |   ..................   | Page20        |  |裏表紙         |
  |               |  |              |                        |               |  |              |
  |               |  |              |                        |               |  |              |
  -----------------  ----------------                        -----------------  ----------------
```

## 使い方

```
python main.py < input.pdf > output.pdf
```

指定可能なオプションは `--first_page [right|left]` のみ。 `first_page` を使って1枚目の左右どちらに表表紙があるかを指定する

## 参考

以下の情報を参考にさせていただきました。
* [見開き中央綴じ資料をスキャンしたPDFをページ毎に分割する](https://qiita.com/hrb23m/items/0a453377d853800fc585)
* [Split pages in pdf](https://unix.stackexchange.com/questions/12482/split-pages-in-pdf/12483#12483)