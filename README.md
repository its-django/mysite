mysite
======
這是書中的程式碼

![cover image](https://github.com/myyang/mysite/blob/master/cover.jpg = 250x)

## git 分支架構

* 每個章節為一個分支(branch)，以module\_XX為分支名稱
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

## 如何使用
取得最新版本程式碼
```
$ git clone git@github.com:myyang/mysite.git
$ cd mysite
```

取得所有的branch
```
$ git fetch
```

若要檢視某章節完成結果，可以切換branch
```
$ git checkout module_XX
```

查看commit簡易hash值及訊息
```
$ git log --oneline
4e829b3 Module_20 - 部署設定檔
3e1572a Module_19 - 使用fixtures預載測試資料
2765b47 Moduel_19 - 登入、登出訪問測試
8873d22 Module_19 - 簡易網站訪問測試
e0120b9 Module_19 - 簡易單元測試
```
假設現在要換到"Module\_19 - 簡易單元測試"，看這時的程式碼是什麼狀況，使用
```
$ git checkout e0120b9
```
此時便回到"Module\_19 - 簡易單元測試"時的開發狀況

> 其他git指令請參考[git官網](http://git-scm.com/book/zh-tw/v1)

## 如何取得書本

###實體書
請參考各出版社合作之[通路](http://books.gotop.com.tw/v_ACL043800)

###電子書
可以在[Google Play](https://play.google.com/store/books/details/%E8%A2%81%E5%85%8B%E5%80%AB_%E6%A5%8A%E5%AD%9F%E7%A9%8E_It_s_Django_%E7%94%A8Python%E8%BF%85%E9%80%9F%E6%89%93%E9%80%A0Web%E6%87%89%E7%94%A8_%E9%9B%BB%E5%AD%90%E6%9B%B8?id=C5UVCgAAQBAJ)上購買
