It's Django -- 用Python迅速打造Web應用 
======
<img src="https://github.com/its-django/mysite/blob/master/cover.jpg" width="150px"/>

* [範例碼](#範例碼)
  * [適用版本](#適用版本)
  * [使用說明](#使用說明)
    * [範例碼分支架構](#範例碼分支架構)
    * [使用git下載與操作](#使用git下載與操作)
    * [代碼打包下載](#代碼打包下載)
* [勘誤](#勘誤) 
* [如何取得本書](#如何取得本書)
* [好評](#好評)

## 範例碼

這裡提供本書讀者關於範例碼的適用版本資訊以及使用方法。

### 適用版本

* [Python2.7](https://www.python.org/downloads/)
* [Django1.7](https://www.djangoproject.com/download/1.7.9/tarball/)

目前書中的範例碼跟說明並不完全適用於Django1.8以上的版本，我們會儘快就此新版本提供更新的說明和範例碼。若本書有機會再版，也會就版本部分進行更新。

### 使用說明

由於本書的範例碼是藉由git管理、github保存，所以讀者如果熟悉git/github的話，可以參考本處所提供的操作說明。不熟悉git/github的朋友也不需要太擔心，我們會提供簡易式的網頁操作方式跟一次性的代碼下載給大家。

* [It's Django 範例碼使用指南(PDF)](https://github.com/myyang/mysite/blob/master/It%27s%20django%20%E7%AF%84%E4%BE%8B%E7%A2%BC%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.pdf)

#### 範例碼分支架構

* 每個章節為一個分支(branch)，以module\_X為分支名稱
* 基本上以每個小節為一個commit，若小節中有多處修改則多次commit
* 當module完成後會merge回master更新, 但module的分支會繼續留著

git分支架構示意圖
```
master-----------m1----m2----m3----m4--.....--m20
    `--module_1--/    /    /
        `--module_2--/    /
            `--module_3--/
                `-- .....
```

#### 使用git下載與操作

如果讀者們有安裝git的話，可以利用下述方法來下載代碼:
```
$ git clone git@github.com:myyang/mysite.git
```

接著利用cd指令進入代碼目錄
```
$ cd mysite
```

接著我們需要取得每個章節分別的內容(各分支)，請在`mysite`資料夾底下輸入
```
$ git fetch
```

然後我們就可以任意地切換到章節X(切到某分支)
```
$ git checkout module_X
```

如果我們要切換到某章節的某次更動狀態，請先查詢代碼(查看commit簡易hash值及訊息)
```
$ git log --oneline
4e829b3 Module_20 - 部署設定檔
3e1572a Module_19 - 使用fixtures預載測試資料
2765b47 Moduel_19 - 登入、登出訪問測試
8873d22 Module_19 - 簡易網站訪問測試
e0120b9 Module_19 - 簡易單元測試
```

假設現在要切換到"Module\_19 - 簡易單元測試"，看這時的程式碼是什麼狀況，只要指定代碼
```
$ git checkout e0120b9
```

此時便回到"Module\_19 - 簡易單元測試"時的開發狀況

> 其他git指令請參考[git官網](http://git-scm.com/book/zh-tw/v1)

#### 代碼打包下載

(盡速提供)

## 勘誤

本書雖歷經數次校稿，但難免有疏漏之處，我們將在這裡提供本書的勘誤。
(盡速提供)

## 如何取得本書

實體書的購買管道請參考各出版社合作之[通路](http://books.gotop.com.tw/v_ACL043800)

電子書可以在[Google Play](https://play.google.com/store/books/details/%E8%A2%81%E5%85%8B%E5%80%AB_%E6%A5%8A%E5%AD%9F%E7%A9%8E_It_s_Django_%E7%94%A8Python%E8%BF%85%E9%80%9F%E6%89%93%E9%80%A0Web%E6%87%89%E7%94%A8_%E9%9B%BB%E5%AD%90%E6%9B%B8?id=C5UVCgAAQBAJ)上購買

## 好評

#### 書評、部落格介紹

[竹亭聽雨](http://q82465.pixnet.net/blog/post/64598949)

#### 銷售成績
