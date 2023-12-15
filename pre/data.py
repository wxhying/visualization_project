from bs4 import BeautifulSoup
import csv
html = """
<html lang="en"><head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="robots" content="all">
  <meta name="author" content="Tencent-TGideas">
  <meta name="Copyright" content="Tencent">
  <meta name="applicable-device" content="pc">
  <title>王者荣耀官方网站-腾讯游戏</title>
  <meta name="description" content="比分、BP、选手对位和出装铭文等数据应有尽有">
  <meta name="keywords" content="王者,赛程,KPL,总决赛">
  <link rel="stylesheet" href="//game.gtimg.cn/images/yxzj/matchdata/reset.css">
  <link rel="stylesheet" href="js/lib/jqTable/css/jqTable.css">
  <link rel="stylesheet" href="//game.gtimg.cn/images/yxzj/matchdata/table.css">
  <link rel="stylesheet" href="//game.gtimg.cn/images/yxzj/matchdata/team.css">
<script type="text/javascript" src="https://pvp.qq.com/m/matchdata/js/ide.js"></script><style>/*
	PC端登录相关样式
	less使用方式：
	lessc login.css login-min.css -x
*/


/*qq登录*/
.milo-qqLogin{
    /*position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;*/
}
.milo-qqLogin .qqLoginCover{
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    z-index: 999;
    background-color: white;
    opacity: 0.7;
    filter: alpha(opacity=70);
}
.milo-qqLogin .qqLoginContent{
    width: 650px;
    height: 400px;
    background-color: #fff;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 10000;
    margin-left: -375px;
    margin-top: -225px;
    border: 1px solid #bfbfbf;
    box-shadow: 0 0 10px rgba(0, 0, 0, .3)
}
.milo-qqLogin .qqLoginFrame{
	width: 100%;
    height: 400px;
    overflow: hidden;
    border: 0px solid white
}

/*微信登录*/
.milo-wxLogin{

}
.milo-wxLogin .wxLoginCover{
	position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    z-index: 999;
    background-color: white;
    opacity: 0.7;
    filter: alpha(opacity=70);
}
.milo-wxLogin .wxLoginContent{
    box-sizing: content-box;
	width: 300px;
    height: 460px;
    background-color: #fff;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 10000;
    margin-left: -150px;
    margin-top: -230px;
    border: 1px solid #bfbfbf;
    box-shadow: 0 0 10px rgba(0, 0, 0, .3);
    padding:0px 20px;
}
.milo-wxLogin .wxLoginContent .wxLoginClose{
    height: 40px;
    width: 100%;  
}
.milo-wxLogin .wxLoginContent .wxLoginClose a{
	line-height: 36px;
    text-align: center;
	float: right;
	margin-right: -20px;
    height: 40px;
    width: 40px;
    display:inline-block;
	color: rgb(102, 102, 102);
    font-family: Verdana, sans-serif;
    font-size: 30px;
    text-decoration:none;
    cursor: pointer;
}
.milo-wxLogin .wxLoginContent .wxLoginClose a:hover{
	color: rgb(240, 115, 115);
    font-family: Verdana, sans-serif;
}
.milo-wxLogin .wxLoginContent .wxLoginBox{
	width:100%;
	height:100%;
	overflow:hidden;
}


/*qq微信登录*/

.milo-qqwx-login {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    display: none
}

.qqwx-login-cover {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    z-index: 9999;
    background-color: white;
    opacity: 0.7;
    filter: alpha(opacity=70)
}

.qqwx-login-frame {
    width: 750px;
    height: 470px;
    background-color: white;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 10000;
    margin-left: -375px;
    margin-top: -240px;
    border: 1px solid #bfbfbf;
    box-shadow: 0 0 10px rgba(0, 0, 0, .3);
    border-radius: 5px 5px 0px 0px;
}

.qqwx-tabs {
    line-height: 40px;
    /* position: absolute; */
    z-index: 100001;
    width: 100%;
    height: 40px;
}

.qqwx-tabs .qq-tab,
.qqwx-tabs .wx-tab {
    cursor: pointer;
    display: inline-block;
    width: 50%;
    float: left;
    text-align: center;
    font-size: 18px;
    background-color: #f1f1f1;
    color: #b1b1b1;
    text-decoration: none
}

.qqwx-active-qq a.qq-tab {
    color: #fff;
    background-color: #51b7ec
}

.qqwx-active-wx a.wx-tab {
    color: #fff;
    background-color: #4ab218
}

.qqwx-tabs .qqwxtab-close {
    position: absolute;
    right: 0px;
    top: 0px;
    text-decoration: none;
    color: grey;
    font-size: 25px;
    line-height: 25px;
    display: inline-block;
    padding: 0px 5px;
    border-width: 0px 0px 1px 1px;
    border-style: solid
}

.qqwx-active-qq .qqwx-tabs .qqwxtab-close {
    border-color: #e0dcdc
}

.qqwx-active-wx .qqwx-tabs .qqwxtab-close {
    border-color: #8BC34A;
    color: #d4d2d2
}

.qqwx-tabs .qqwxtab-close:hover {
    font-weight: bold
}

.qqwx-tips {
    line-height: 30px;
    font-size: 14px;
    text-align: center;
    color: #a2a2a2;
    position: absolute;
    height: 32px;
    width: 100%;
    top: 40px;
    z-index: 10001;
    background-color: #fff;
    border: none;
}

.qqwx-frame {
    width: 100%;
    height: 400px;
    position: absolute;
    overflow: hidden;
    border: none;
    top: 70px;
}

.qqwx-frame div {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0px;
    top: 0px;
    text-align: center;
    display: none;
    border: none;
}

.qqwx-frame div iframe {
    width: 100%;
    height: 100%;
    border: none;
}

.qqwx-active-qq div.qqwx-frame-qq-div {
    display: block
}

.qqwx-active-wx div.qqwx-frame-wx-div {
    display: block
}

i.ico-qq-logo,
i.ico-wx-logo {
    display: inline-block;
    height: 23px;
    vertical-align: middle;
    margin: 0px 5px;
    margin-top: -4px;
    background: url(https://vm.gtimg.cn/tencentvideo/vstyle/web/common/style/img/login/sprite_login.png?d=0210&max_age=31104000) no-repeat
}

i.ico-qq-logo {
    width: 20px
}

i.ico-wx-logo {
    width: 24px
}

.qqwx-active-wx i.ico-qq-logo {
    background-position: -180px -90px
}

.qqwx-active-wx i.ico-wx-logo {
    background-position: -250px -90px
}

.qqwx-active-qq i.ico-qq-logo {
    background-position: -200px -90px
}

.qqwx-active-qq i.ico-wx-logo {
    background-position: -220px -90px
}

div#qqwx-frame-wx-div {
    top: 20px
}


/*qc登录*/

.loginframe {
    width: 100%;
    height: 400px;
    overflow: hidden;
    border: 0px solid white
}

.milo-qConnectLogin {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px
}

.qConnectLoginCover {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    z-index: 9999;
    background-color: white;
    opacity: 0.7;
    filter: alpha(opacity=70)
}

.qConnectLoginContent {
    width: 752px;
    height: 400px;
    background-color: #fff;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 10000;
    margin-left: -375px;
    margin-top: -220px;
    border: 1px solid #bfbfbf;
    box-shadow: 0 0 10px rgba(0, 0, 0, .3)
}

.qConnectLoginContent>div {
    height: 30px;
    width: 100%;
    background-color: #4fb7ec;
    font-size: 18px
}

.qConnectLoginContent>div span {
    color: white;
    display: inline-block;
    line-height: 30px;
    padding: 0px 5px
}

.qConnectLoginContent>div a {
    float: right;
    line-height: 30px;
    text-decoration: none;
    color: white;
    font-weight: bold;
    font-size: 25px;
    width: 30px;
    text-align: center;
    cursor: pointer
}

.qConnectLoginContent>div a:hover {
    color: #f57272
}

.qConnectLoginContent>div {
    position: absolute;
    z-index: 100001;
    right: 0px;
    width: 30px;
    top: 0px;
    height: 48px;
    text-align: center
}

.qConnectLoginContent>div a {
    line-height: 40px;
    display: inline-block
}


/*qc微信登录*/

.milo-qcwx-login {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    display: none
}

.qcwx-login-cover {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    z-index: 9999;
    background-color: white;
    opacity: 0.7;
    filter: alpha(opacity=70)
}

.qcwx-login-frame {
    width: 750px;
    height: 470px;
    background-color: white;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 10000;
    margin-left: -375px;
    margin-top: -240px;
    border: 1px solid #bfbfbf;
    box-shadow: 0 0 10px rgba(0, 0, 0, .3);
    border-radius: 5px 5px 0px 0px;
}

.qcwx-tabs {
    line-height: 40px;
    position: absolute;
    z-index: 100001;
    width: 100%
}

.qcwx-tabs .qc-tab,
.qcwx-tabs .wx-tab {
    cursor: pointer;
    display: inline-block;
    width: 50%;
    float: left;
    text-align: center;
    font-size: 18px;
    background-color: #f1f1f1;
    color: #b1b1b1;
    text-decoration: none
}

.qcwx-active-qc a.qc-tab {
    color: #fff;
    background-color: #51b7ec
}

.qcwx-active-wx a.wx-tab {
    color: #fff;
    background-color: #4ab218
}

.qcwx-tabs .qcwxtab-close {
    position: absolute;
    right: 0px;
    top: 0px;
    text-decoration: none;
    color: grey;
    font-size: 25px;
    line-height: 25px;
    display: inline-block;
    padding: 0px 5px;
    border-width: 0px 0px 1px 1px;
    border-style: solid
}

.qcwx-active-qc .qcwx-tabs .qcwxtab-close {
    border-color: #e0dcdc
}

.qcwx-active-wx .qcwx-tabs .qcwxtab-close {
    border-color: #8BC34A;
    color: #d4d2d2
}

.qcwx-tabs .qcwxtab-close:hover {
    font-weight: bold
}

.qcwx-tips {
    line-height: 30px;
    font-size: 14px;
    text-align: center;
    color: #a2a2a2;
    position: absolute;
    width: 100%;
    top: 40px;
    z-index: 10001;
    background-color: #fff;
}

.qcwx-frame {
    width: 750px;
    height: 470px;
    position: absolute;
    overflow: hidden;
}

.qcwx-frame div {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0px;
    top: 0px;
    text-align: center;
    display: none
}

.qcwx-frame div iframe {
    width: 100%;
    height: 100%
}

.qcwx-active-qc div.qcwx-frame-qc-div {
    display: block
}

.qcwx-active-wx div.qcwx-frame-wx-div {
    display: block;
    top: 70px;
    height: 400px;
}

i.ico-qc-logo,
i.ico-wx-logo {
    display: inline-block;
    height: 23px;
    vertical-align: middle;
    margin: 0px 5px;
    margin-top: -4px;
    background: url(https://vm.gtimg.cn/tencentvideo/vstyle/web/common/style/img/login/sprite_login.png?d=0210&max_age=31104000) no-repeat
}

i.ico-qc-logo {
    width: 20px
}

i.ico-wx-logo {
    width: 24px
}

.qcwx-active-wx i.ico-qc-logo {
    background-position: -180px -90px
}

.qcwx-active-wx i.ico-wx-logo {
    background-position: -250px -90px
}

.qcwx-active-qc i.ico-qc-logo {
    background-position: -200px -90px
}

.qcwx-active-qc i.ico-wx-logo {
    background-position: -220px -90px
}

div#qcwx-frame-wx-div {
    top: 20px
}


/*wegame登录*/

.wegameloginframe {
    width: 100%;
    height: 600px;
    overflow: hidden;
    border: 0px solid white
}

.milo-wegameLogin {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px
}

.wegameLoginCover {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    z-index: 9999;
    background-color: white;
    opacity: 0.7;
    filter: alpha(opacity=70)
}

.wegameLoginContent {
    width: 800px;
    height: 600px;
    background-color: #fff;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 10000;
    margin-left: -400px;
    margin-top: -300px;
    border: 1px solid #bfbfbf;
    box-shadow: 0 0 10px rgba(0, 0, 0, .3)
}

.wegameLoginContent>div {
    height: 30px;
    width: 100%;
    background-color: none;
    font-size: 18px
}

.wegameLoginContent>div.wegameLoginTitle {
    width: 100%;
    background-color: #0e0e0e
}

div.wegameLoginIcon {
    display: none
}

.wegameLoginTitle>div.wegameLoginIcon {
    display: block;
    float: left;
    width: 239px;
    height: 60px;
    background: url(https://api.rail.tgp.qq.com/web/oauth2.0/login/images/wegame-logo-m.png) no-repeat center;
    margin-left: 10px
}

.wegameLoginContent>div span {
    color: white;
    display: inline-block;
    line-height: 30px;
    padding: 0px 5px
}

.wegameLoginContent>div a {
    float: right;
    line-height: 30px;
    text-decoration: none;
    color: white;
    font-weight: bold;
    font-size: 25px;
    width: 30px;
    text-align: center;
    cursor: pointer
}

.wegameLoginContent>div a:hover {
    color: #f57272
}

.wegameLoginContent>div {
    position: absolute;
    z-index: 100001;
    right: 0px;
    width: 30px;
    top: 0px;
    height: 60px;
    text-align: center
}

.wegameLoginContent>div a {
    line-height: 55px;
    display: inline-block
}

</style><style>.ide-dialog__wrapper {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  overflow: auto;
  margin: 0;
}
.ide-dialog__wrapper .ide-dialog {
  position: relative;
  margin: 100px auto;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 3px rgba(0,0,0,0.3);
  box-shadow: 0 1px 3px rgba(0,0,0,0.3);
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  width: 300px;
  background-color: #fff;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__header {
  padding: 20px 20px 10px;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__header .ide-dialog__title {
  line-height: 24px;
  font-size: 18px;
  color: #303133;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__header .ide-dialog__headerbtn {
  position: absolute;
  top: 20px;
  right: 20px;
  padding: 0;
  background: 0 0;
  border: none;
  outline: 0;
  cursor: pointer;
  font-size: 16px;
  color: #909399;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__header .ide-dialog__headerbtn:focus,
.ide-dialog__wrapper .ide-dialog .ide-dialog__header .ide-dialog__headerbtn :hover {
  color: #409eff;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__body {
  padding: 30px 20px;
  color: #606266;
  font-size: 14px;
  word-break: break-all;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__footer {
  padding: 10px 20px 20px;
  text-align: right;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__footer .ide-button {
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  background: #fff;
  border: 1px solid #dcdfe6;
  color: #606266;
  -webkit-appearance: none;
  text-align: center;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  outline: 0;
  margin: 0 5px;
  -webkit-transition: 0.1s;
  transition: 0.1s;
  font-weight: 500;
  padding: 12px 20px;
  font-size: 14px;
  border-radius: 4px;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__footer .ide-button:focus,
.ide-dialog__wrapper .ide-dialog .ide-dialog__footer .ide-button:hover {
  color: #409eff;
  border-color: #c6e2ff;
  background-color: #ecf5ff;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__footer .ide-button.primary {
  background: #3a8ee6;
  border-color: #3a8ee6;
  color: #fff;
}
.ide-dialog__wrapper .ide-dialog .ide-dialog__footer .ide-button.primary:focus,
.ide-dialog__wrapper .ide-dialog .ide-dialog__footer .ide-button.primary:hover {
  background: #66b1ff;
  border-color: #66b1ff;
  color: #fff;
}
.ide-dialog-mask {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  opacity: 0.5;
  background: #000;
  z-index: 2002;
}
</style><style>.item {
  line-height: 45px;
  font-size: 14px;
  padding: 3px 0;
  width: 100%;
}
.item select {
  background-color: #fff;
  background-image: none;
  border-radius: 4px;
  border: 1px solid #dcdfe6;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  color: #606266;
  display: inline-block;
  font-size: inherit;
  height: 40px;
  line-height: 40px;
  outline: 0;
  padding: 0 15px;
  -webkit-transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
  transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
  width: 100%;
}
/*.ide-PIPContainer{
  display: block;
}*/
.ide-PIPInfo {
  margin-right: 5px;
  border: 1px solid #dcdfe6;
  -webkit-appearance: checkbox;
}
#ide-error-message {
  display: none;
  color: #f00;
}
</style><style>.jFrankContainer {
  display: table;
  width: 100%;
}
.jFrankContainer thead {
  color: #909399;
  font-weight: 500;
}
.jFrankContainer td {
  font-size: 14px;
  color: #606266;
}
.jFrankContainer td,
.jFrankContainer th {
  padding: 12px 0;
  min-width: 0;
  box-sizing: border-box;
  text-overflow: ellipsis;
  vertical-align: middle;
  position: relative;
  text-align: left;
  border-bottom: 1px solid #ebeef5;
}
.jFrankContainer td .cell,
.jFrankContainer th .cell {
  display: inline-block;
  box-sizing: border-box;
  position: relative;
  vertical-align: middle;
  padding-left: 10px;
  padding-right: 10px;
  width: 100%;
}
</style><style>.ide-form-label {
  vertical-align: middle;
  float: left;
  width: 100px;
  font-size: 14px;
  color: #606266;
  line-height: 30px;
  padding: 0 12px 0 0;
  box-sizing: border-box;
}
.ide-form-label.is-require:before {
  content: "*";
  color: #f56c6c;
  margin-right: 4px;
}
.ide-form-item {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  border-radius: 4px;
  border: 1px solid #dcdfe6;
  box-sizing: border-box;
  color: #606266;
  display: inline-block;
  font-size: inherit;
  height: 40px;
  outline: none;
  padding: 0 15px;
  transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
  width: 250px;
}
.ide-form-row {
  clear: both;
}
.ide-personInfo textarea {
  height: 70px !important;
}
.ide-dialog__body {
  padding: 10px 20px !important;
}
.ide-form-contariner {
  line-height: 40px;
  position: relative;
  font-size: 14px;
  display: inline-block;
  margin-bottom: 5px;
}
</style><style>#ide-paginator {
  font-size: 14px;
  overflow: hidden;
  margin: 0 auto;
  text-align: center;
  color: #333;
  display: flex;
  padding: 10px 5px;
  justify-content: center;
  align-items: center;
}
#ide-paginator .my-page-prev,
#ide-paginator .my-page-next {
  float: left;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  border: 1px solid #ddd;
  cursor: pointer;
}
#ide-paginator .my-page-prev:hover,
#ide-paginator .my-page-next:hover {
  color: #409eff;
}
#ide-paginator .my-page-prev.my-page-forbid,
#ide-paginator .my-page-next.my-page-forbid {
  pointer-events: none;
  background-color: #f4f4f5;
  color: rgba(0,0,0,0.2);
}
#ide-paginator .my-page-group {
  float: left;
  margin: 0;
  padding: 0;
  overflow: hidden;
}
#ide-paginator .my-page-group li {
  float: left;
  list-style: none;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  min-width: 30px;
  padding: 0 8px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  margin: 0 5px;
  cursor: pointer;
}
#ide-paginator .my-page-group .my-page-cell {
  border: 1px solid #ddd;
  border-radius: 2px;
}
#ide-paginator .my-page-group .my-page-cell.my-page-checked {
  background-color: #409eff;
  color: #fff;
}
#ide-paginator .my-page-group .my-page-omit {
  pointer-events: none;
}
.lotteryRecordContainer table {
  display: table;
  width: 100%;
}
.lotteryRecordContainer table thead {
  color: #909399;
  font-weight: 500;
}
.lotteryRecordContainer table td {
  font-size: 14px;
  color: #606266;
}
.lotteryRecordContainer table td,
.lotteryRecordContainer table th {
  padding: 12px 0;
  min-width: 0;
  box-sizing: border-box;
  text-overflow: ellipsis;
  vertical-align: middle;
  position: relative;
  text-align: left;
  border-bottom: 1px solid #ebeef5;
}
.lotteryRecordContainer table td .cell,
.lotteryRecordContainer table th .cell {
  display: inline-block;
  box-sizing: border-box;
  position: relative;
  vertical-align: middle;
  padding-left: 10px;
  padding-right: 10px;
  width: 100%;
}
</style><style>#ide-broadcast {
  height: 140px;
  overflow: hidden;
}
#ide-broadcast ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
#ide-broadcast ul li {
  margin: 0;
  padding: 0;
}
</style><style>.ide-role-item {
  margin-bottom: 15px;
}
.ide-form-label {
  width: 100px;
  height: 40px;
  white-space: nowrap;
}
#ide-cdkey-verify {
  margin-top: 15px;
}
#ide-verifyImg {
  margin-top: 10px;
  width: 150px;
  height: 50px;
  cursor: pointer;
}
</style></head>

<body>
  <div class="page">
    <div class="header">
      <div class="header-box withMain">
        <div class="headerLeft">
          <a href="https://pvp.qq.com/matchdata/index.html">
          <div class="imgBox">
            <img class="img1" src="//game.gtimg.cn/images/yxzj/matchdata/logo3.png" alt="王者荣耀">
          </div>
          <div class="imgBox1">
            <img class="img2" src="//game.gtimg.cn/images/yxzj/matchdata/logo2.png" alt="王者荣耀数据平台">
          </div>
        </a>
        </div>
        <div class="headerRight">
          <ul class="menu clearfix">
            <li>
              <a data-url="https://pvp.qq.com/matchdata/schedule.html" href="https://pvp.qq.com/matchdata/schedule.html?league_id=20230001">赛程</a>
            </li>
            <li> <a data-url="https://pvp.qq.com/matchdata/teamData.html" href="https://pvp.qq.com/matchdata/teamData.html?league_id=20230001">战队数据</a></li>
            <li class="active"> <a data-url="https://pvp.qq.com/matchdata/playerData.html" href="https://pvp.qq.com/matchdata/playerData.html?league_id=20230001">选手数据</a></li>
            <li> <a data-url="https://pvp.qq.com/matchdata/heroData.html" href="https://pvp.qq.com/matchdata/heroData.html?league_id=20230001">英雄数据</a></li>
          </ul>
          <div class="login-text fr">
              <a style="color: #BDC4C7;" target="_blank" href="https://prod.comp.smoba.qq.com/eh/index.html">
                <i class="safe"></i>
                <span class="text">荣誉殿堂</span>
              </a>
            <img class="user" src="//game.gtimg.cn/images/yxzj/matchdata/user.png" alt="">
            <span class="nologin">亲爱的召唤师，欢迎<i class="login" onclick="logins()">登录</i> </span>
            <span class="islogin" style="display: none">欢迎你，<span class="nick-name">召唤师</span><i class="login" onclick="logouts()">登出</i> </span>
          </div>
        </div>
      </div>
    </div>
    <div class="content-box withMain">
      <div class="content-left">
        <div class="team-left-title">赛事</div>
        <ul class="competition-list"><li league-id="20230004" is_hok="true">
            <div class="shadow-bg">
              <p class="shadow-time">2023年</p>
              <p class="shadow-text">王者荣耀世界冠军杯</p>
            </div>
            <div class="status-tag">进行中-常规赛</div>
            <div class="imgbox">
              <img src="https://smobatv-pic.tga.qq.com/fbc42171de8c11964468fd98ac27fdae.png" alt="2023年王者荣耀世界冠军杯">
            </div>
            <div class="cl-text">
              <p class="cl-name">2023年王者荣耀世界冠军杯</p>
              <p class="cl-time">2023.11.13~2023.12.31</p>
            </div>
          </li><li league-id="20230003" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2023年</p>
              <p class="shadow-text">王者荣耀挑战者杯</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://smobatv-pic.tga.qq.com/228037f3c775bb2158edbe3366541e0d.png" alt="2023年王者荣耀挑战者杯">
            </div>
            <div class="cl-text">
              <p class="cl-name">2023年王者荣耀挑战者杯</p>
              <p class="cl-time">2023.10.13~2023.11.05</p>
            </div>
          </li><li league-id="20230002" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2023年</p>
              <p class="shadow-text">KPL夏季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://smobatv-pic.tga.qq.com/b1ecf9198a9277e437de5a707de13bef.png" alt="2023年KPL夏季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2023年KPL夏季赛</p>
              <p class="cl-time">2023.06.14~2023.09.10</p>
            </div>
          </li><li class="active" league-id="20230001" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2023年</p>
              <p class="shadow-text">KPL春季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://smobatv-pic.tga.qq.com/d61f68a4aa435427392d070c80ef86e4.png" alt="2023年KPL春季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2023年KPL春季赛</p>
              <p class="cl-time">2023.02.10~2023.06.02</p>
            </div>
          </li><li league-id="20220003" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2022年</p>
              <p class="shadow-text">王者荣耀挑战者杯</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="http://dldir1.qq.com/tgatv/wzry_tv/2022challenger/kv/2022tiaozhanzhebei01.jpg" alt="2022年王者荣耀挑战者杯">
            </div>
            <div class="cl-text">
              <p class="cl-name">2022年王者荣耀挑战者杯</p>
              <p class="cl-time">2022.09.13~2022.10.08</p>
            </div>
          </li><li league-id="20220002" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2022年</p>
              <p class="shadow-text">KPL夏季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="http://dldir1.qq.com/tgatv/wzry_tv/2022KPLsummer/2022KPLsummerkaisai.jpg" alt="2022年KPL夏季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2022年KPL夏季赛</p>
              <p class="cl-time">2022.06.08~2022.09.08</p>
            </div>
          </li><li league-id="20220001" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2022年</p>
              <p class="shadow-text">KPL春季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/KPL2022S1.jpg" alt="2022年KPL春季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2022年KPL春季赛</p>
              <p class="cl-time">2022.02.09~2022.05.08</p>
            </div>
          </li><li league-id="20210005" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2021年</p>
              <p class="shadow-text">王者荣耀挑战者杯</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20210005.jpg" alt="2021年王者荣耀挑战者杯">
            </div>
            <div class="cl-text">
              <p class="cl-name">2021年王者荣耀挑战者杯</p>
              <p class="cl-time">2021.12.31~2022.01.15</p>
            </div>
          </li><li league-id="20210004" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2021年</p>
              <p class="shadow-text">KPL秋季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20210004.jpg" alt="2021KPL秋季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2021KPL秋季赛</p>
              <p class="cl-time">2021.09.22~2021.12.25</p>
            </div>
          </li><li league-id="20210003" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2021年</p>
              <p class="shadow-text">世界冠军杯</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/league_75a3c08081a511eb81f6140564711851.png" alt="2021世界冠军杯">
            </div>
            <div class="cl-text">
              <p class="cl-name">2021世界冠军杯</p>
              <p class="cl-time">2021.07.05~2021.08.28</p>
            </div>
          </li><li league-id="202100201" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2021年</p>
              <p class="shadow-text">KPL春季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/league_2005864c8e1911ebb99320906f5a1b8f.png" alt="2021KPL春季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2021KPL春季赛</p>
              <p class="cl-time">2021.03.27~2021.06.25</p>
            </div>
          </li><li league-id="20210021" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2021年</p>
              <p class="shadow-text">KPL春季赛季前赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/league_2005864c8e1911ebb99320906f5a1b8f.png" alt="2021KPL春季赛季前赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2021KPL春季赛季前赛</p>
              <p class="cl-time">2021.03.11~2021.03.21</p>
            </div>
          </li><li league-id="20200005" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2020年</p>
              <p class="shadow-text">冬季冠军杯</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20200005.jpg" alt="2020冬季冠军杯">
            </div>
            <div class="cl-text">
              <p class="cl-name">2020冬季冠军杯</p>
              <p class="cl-time">2021.01.06~2021.01.23</p>
            </div>
          </li><li league-id="20200004" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2020年</p>
              <p class="shadow-text">KPL秋季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20200004.jpg" alt="2020KPL秋季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2020KPL秋季赛</p>
              <p class="cl-time">2020.09.16~2020.12.19</p>
            </div>
          </li><li league-id="20200003" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2020年</p>
              <p class="shadow-text">世界冠军杯正赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20200002.jpg" alt="2020世界冠军杯正赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2020世界冠军杯正赛</p>
              <p class="cl-time">2020.07.15~2020.08.16</p>
            </div>
          </li><li league-id="20200002" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2020年</p>
              <p class="shadow-text">世界冠军杯选拔赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20200002.jpg" alt="2020世界冠军杯选拔赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2020世界冠军杯选拔赛</p>
              <p class="cl-time">2020.06.22~2020.06.28</p>
            </div>
          </li><li league-id="20200001" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2020年</p>
              <p class="shadow-text">KPL春季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20200001.jpg" alt="2020KPL春季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2020KPL春季赛</p>
              <p class="cl-time">2020.03.22~2020.06.13</p>
            </div>
          </li><li league-id="20190006" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2019年</p>
              <p class="shadow-text">冬季冠军杯</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20190006.png" alt="2019冬季冠军杯">
            </div>
            <div class="cl-text">
              <p class="cl-name">2019冬季冠军杯</p>
              <p class="cl-time">2019.12.21~2020.01.05</p>
            </div>
          </li><li league-id="20190004" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2019年</p>
              <p class="shadow-text">KPL秋季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20190004.jpg" alt="2019KPL秋季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2019KPL秋季赛</p>
              <p class="cl-time">2019.09.11~2019.12.14</p>
            </div>
          </li><li league-id="20190003" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2019年</p>
              <p class="shadow-text">世界冠军杯正赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20190003.jpg" alt="2019世界冠军杯正赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2019世界冠军杯正赛</p>
              <p class="cl-time">2019.07.10~2019.08.10</p>
            </div>
          </li><li league-id="20190002" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2019年</p>
              <p class="shadow-text">世界冠军杯选拔赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20190002.jpg" alt="2019世界冠军杯选拔赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2019世界冠军杯选拔赛</p>
              <p class="cl-time">2019.06.06~2019.06.09</p>
            </div>
          </li><li league-id="20190001" is_hok="false">
            <div class="shadow-bg">
              <p class="shadow-time">2019年</p>
              <p class="shadow-text">KPL春季赛</p>
            </div>
            <div class="status-tag">已结束-常规赛</div>
            <div class="imgbox">
              <img src="https://res.edata.qq.com/sgame/static/images/league/20190001.jpg" alt="2019KPL春季赛">
            </div>
            <div class="cl-text">
              <p class="cl-name">2019KPL春季赛</p>
              <p class="cl-time">2019.03.06~2019.06.02</p>
            </div>
          </li></ul>
      </div>

      <div class="content-right">
        <div class="table-box" id="rtable" style="">
          <div>
            <div class="c-table--main c-table c-table--noWrap c-table--border c-table--fit c-table__cell--block" style="width: 100%; max-height: 542px;"><div class="c-table__header-wrapper"> <table cellspacing="0" cellpadding="0" border="0" role="c-table1" data-height="542" class="c-table__header" style="width: 2348px; margin-left: 0px;">
              <colgroup id="colgroup"><col name="" width="100"><col name="" width="133"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="113"></colgroup>
              <thead>
                <tr id="table-header">
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">排名</div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p pop-team">
                        选手
                        <img class="sx-icon" src="//game.gtimg.cn/images/yxzj/matchdata/sx.png" width="11px" height="12px" alt="" srcset="">
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        比赛场次 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        胜场 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        胜率 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均KDA <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均击杀数 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均死亡数 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均助攻数 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均经济 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        分均经济 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        经济占比 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均伤害 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        分均伤害 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        伤害占比 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        伤害转化率 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均承伤 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        分均承伤 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        承伤占比 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均推塔数 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        推搭占比 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        参团率 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均比赛时长 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                </tr>
              </thead>
              
            </table></div><div class="c-table__body-wrapper" style="max-height: 497.4px;"> <table cellspacing="0" cellpadding="0" border="0" role="c-table1" data-height="542" class="c-table__body" style="width: 2348px;">
              <colgroup id="colgroup"><col name="" width="100"><col name="" width="133"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="113"></colgroup>
              
              <tbody><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/38e591cf1ed8efa83ea56f34bbb88af7.png" alt="花月" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">花月</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">100%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">9</span>
                      <span class="kda2">5 / 1 / 4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">7554</div>
                  </td>
                  <td>
                    <div class="cell">755</div>
                  </td>
                  <td>
                    <div class="cell">21%</div>
                  </td>
                  <td>
                    <div class="cell">49291</div>
                  </td>
                  <td>
                    <div class="cell">4518.5</div>
                  </td>
                  <td>
                    <div class="cell">21.8%</div>
                  </td>
                  <td>
                    <div class="cell">103.9%</div>
                  </td>
                  <td>
                    <div class="cell">23929</div>
                  </td>
                  <td>
                    <div class="cell">1832.3</div>
                  </td>
                  <td>
                    <div class="cell">14.8%</div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">37.5%</div>
                  </td>
                  <td>
                    <div class="cell">75%</div>
                  </td>
                  <td>
                    <div class="cell">00:10:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/c5f03a87d36aef19a400d1d09365a35a.png" alt="无铭" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">无铭</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">100%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">11.5</span>
                      <span class="kda2">0 / 1 / 11.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">11.5</div>
                  </td>
                  <td>
                    <div class="cell">6248.5</div>
                  </td>
                  <td>
                    <div class="cell">475</div>
                  </td>
                  <td>
                    <div class="cell">13.6%</div>
                  </td>
                  <td>
                    <div class="cell">19384.5</div>
                  </td>
                  <td>
                    <div class="cell">1341.6</div>
                  </td>
                  <td>
                    <div class="cell">6.4%</div>
                  </td>
                  <td>
                    <div class="cell">47.1%</div>
                  </td>
                  <td>
                    <div class="cell">50835.5</div>
                  </td>
                  <td>
                    <div class="cell">3075</div>
                  </td>
                  <td>
                    <div class="cell">23.2%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">6.2%</div>
                  </td>
                  <td>
                    <div class="cell">77.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:14:26</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/b3dcd48a50cc8b4fd2a3479614157382.png" alt="自渡" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">自渡</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">100%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">8</span>
                      <span class="kda2">1 / 0 / 7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">7</div>
                  </td>
                  <td>
                    <div class="cell">6322</div>
                  </td>
                  <td>
                    <div class="cell">632</div>
                  </td>
                  <td>
                    <div class="cell">17.6%</div>
                  </td>
                  <td>
                    <div class="cell">31683</div>
                  </td>
                  <td>
                    <div class="cell">2904.3</div>
                  </td>
                  <td>
                    <div class="cell">14%</div>
                  </td>
                  <td>
                    <div class="cell">79.8%</div>
                  </td>
                  <td>
                    <div class="cell">51490</div>
                  </td>
                  <td>
                    <div class="cell">4251.1</div>
                  </td>
                  <td>
                    <div class="cell">34.3%</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">12.5%</div>
                  </td>
                  <td>
                    <div class="cell">66%</div>
                  </td>
                  <td>
                    <div class="cell">00:10:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/de4b9d54a1c9bfdffea83e29080e0aa9.png" alt="归期" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">归期</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">6</div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">83.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.3</span>
                      <span class="kda2">2.5 / 1.3 / 4.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">4.3</div>
                  </td>
                  <td>
                    <div class="cell">9835.1</div>
                  </td>
                  <td>
                    <div class="cell">649.5</div>
                  </td>
                  <td>
                    <div class="cell">19.7%</div>
                  </td>
                  <td>
                    <div class="cell">51265.6</div>
                  </td>
                  <td>
                    <div class="cell">3202</div>
                  </td>
                  <td>
                    <div class="cell">17.5%</div>
                  </td>
                  <td>
                    <div class="cell">89.8%</div>
                  </td>
                  <td>
                    <div class="cell">72338.8</div>
                  </td>
                  <td>
                    <div class="cell">3703.2</div>
                  </td>
                  <td>
                    <div class="cell">22.5%</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">14.5%</div>
                  </td>
                  <td>
                    <div class="cell">62.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:28</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/3131a3a52761b06dcb89c5ab7f66e52e.png" alt="风劫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">风劫</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">80%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.2</span>
                      <span class="kda2">3.6 / 2.6 / 5.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3.6</div>
                  </td>
                  <td>
                    <div class="cell">2.6</div>
                  </td>
                  <td>
                    <div class="cell">5.4</div>
                  </td>
                  <td>
                    <div class="cell">13112.8</div>
                  </td>
                  <td>
                    <div class="cell">743</div>
                  </td>
                  <td>
                    <div class="cell">23.7%</div>
                  </td>
                  <td>
                    <div class="cell">97282.4</div>
                  </td>
                  <td>
                    <div class="cell">5247.4</div>
                  </td>
                  <td>
                    <div class="cell">26.6%</div>
                  </td>
                  <td>
                    <div class="cell">112.1%</div>
                  </td>
                  <td>
                    <div class="cell">70503</div>
                  </td>
                  <td>
                    <div class="cell">2951.7</div>
                  </td>
                  <td>
                    <div class="cell">16.1%</div>
                  </td>
                  <td>
                    <div class="cell">3.6</div>
                  </td>
                  <td>
                    <div class="cell">47%</div>
                  </td>
                  <td>
                    <div class="cell">73.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:18:27</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/63c9ee50a54d077c0d7af79e59c0b7cc.png" alt="月色" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">月色</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">8</div>
                  </td>
                  <td>
                    <div class="cell">6</div>
                  </td>
                  <td>
                    <div class="cell">75%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.1</span>
                      <span class="kda2">0.5 / 1.6 / 6.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">6.8</div>
                  </td>
                  <td>
                    <div class="cell">10407.1</div>
                  </td>
                  <td>
                    <div class="cell">603.6</div>
                  </td>
                  <td>
                    <div class="cell">19.2%</div>
                  </td>
                  <td>
                    <div class="cell">116158.1</div>
                  </td>
                  <td>
                    <div class="cell">6026.9</div>
                  </td>
                  <td>
                    <div class="cell">28.6%</div>
                  </td>
                  <td>
                    <div class="cell">148.2%</div>
                  </td>
                  <td>
                    <div class="cell">46715.5</div>
                  </td>
                  <td>
                    <div class="cell">2136.2</div>
                  </td>
                  <td>
                    <div class="cell">11.9%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">1.3%</div>
                  </td>
                  <td>
                    <div class="cell">65.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a2a8b6d77f5f3f921406de464abe3216.png" alt="钟意" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">钟意</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">11</div>
                  </td>
                  <td>
                    <div class="cell">8</div>
                  </td>
                  <td>
                    <div class="cell">72.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">6.2</span>
                      <span class="kda2">3 / 1.7 / 5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">12402.3</div>
                  </td>
                  <td>
                    <div class="cell">743.9</div>
                  </td>
                  <td>
                    <div class="cell">23.9%</div>
                  </td>
                  <td>
                    <div class="cell">57220.6</div>
                  </td>
                  <td>
                    <div class="cell">3316.3</div>
                  </td>
                  <td>
                    <div class="cell">16.9%</div>
                  </td>
                  <td>
                    <div class="cell">72.4%</div>
                  </td>
                  <td>
                    <div class="cell">97741.9</div>
                  </td>
                  <td>
                    <div class="cell">3933.8</div>
                  </td>
                  <td>
                    <div class="cell">21.7%</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">19.1%</div>
                  </td>
                  <td>
                    <div class="cell">69%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/60d74420e4df0e080b29c307368dacc6.png" alt="帆帆" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">帆帆</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">60</div>
                  </td>
                  <td>
                    <div class="cell">42</div>
                  </td>
                  <td>
                    <div class="cell">70%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">7.1</span>
                      <span class="kda2">0.8 / 1.2 / 8.1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">8.1</div>
                  </td>
                  <td>
                    <div class="cell">7110.5</div>
                  </td>
                  <td>
                    <div class="cell">454.3</div>
                  </td>
                  <td>
                    <div class="cell">14.5%</div>
                  </td>
                  <td>
                    <div class="cell">38638.1</div>
                  </td>
                  <td>
                    <div class="cell">2241.5</div>
                  </td>
                  <td>
                    <div class="cell">10.8%</div>
                  </td>
                  <td>
                    <div class="cell">75.2%</div>
                  </td>
                  <td>
                    <div class="cell">71765.4</div>
                  </td>
                  <td>
                    <div class="cell">3672.4</div>
                  </td>
                  <td>
                    <div class="cell">21.4%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2.8%</div>
                  </td>
                  <td>
                    <div class="cell">79.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:17</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ca303f0f42b7ce8619dc433c3ed69b23.png" alt="妖刀" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">妖刀</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">75</div>
                  </td>
                  <td>
                    <div class="cell">52</div>
                  </td>
                  <td>
                    <div class="cell">69.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">6</span>
                      <span class="kda2">3.2 / 1.4 / 4.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3.2</div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">4.6</div>
                  </td>
                  <td>
                    <div class="cell">11987.5</div>
                  </td>
                  <td>
                    <div class="cell">756.5</div>
                  </td>
                  <td>
                    <div class="cell">24.3%</div>
                  </td>
                  <td>
                    <div class="cell">88852.2</div>
                  </td>
                  <td>
                    <div class="cell">5265.2</div>
                  </td>
                  <td>
                    <div class="cell">26.4%</div>
                  </td>
                  <td>
                    <div class="cell">107.8%</div>
                  </td>
                  <td>
                    <div class="cell">62970.5</div>
                  </td>
                  <td>
                    <div class="cell">2837.4</div>
                  </td>
                  <td>
                    <div class="cell">16.4%</div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">38.9%</div>
                  </td>
                  <td>
                    <div class="cell">70.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">10</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a5f65ff7a7665af4718b90f48b76789c.png" alt="小胖" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小胖</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">64</div>
                  </td>
                  <td>
                    <div class="cell">44</div>
                  </td>
                  <td>
                    <div class="cell">68.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.4</span>
                      <span class="kda2">2.7 / 1.6 / 4.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.7</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">4.6</div>
                  </td>
                  <td>
                    <div class="cell">11793.1</div>
                  </td>
                  <td>
                    <div class="cell">750</div>
                  </td>
                  <td>
                    <div class="cell">24%</div>
                  </td>
                  <td>
                    <div class="cell">64148.5</div>
                  </td>
                  <td>
                    <div class="cell">3941.9</div>
                  </td>
                  <td>
                    <div class="cell">20%</div>
                  </td>
                  <td>
                    <div class="cell">84.2%</div>
                  </td>
                  <td>
                    <div class="cell">97764</div>
                  </td>
                  <td>
                    <div class="cell">4186.4</div>
                  </td>
                  <td>
                    <div class="cell">24.5%</div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">22%</div>
                  </td>
                  <td>
                    <div class="cell">70.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:18</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">11</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/3109a021ad37fbc536c5dc51405b8654.png" alt="向鱼" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">向鱼</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">67</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">68.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">6.2</span>
                      <span class="kda2">2.2 / 1.2 / 5.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">5.2</div>
                  </td>
                  <td>
                    <div class="cell">8693.5</div>
                  </td>
                  <td>
                    <div class="cell">554.1</div>
                  </td>
                  <td>
                    <div class="cell">17.8%</div>
                  </td>
                  <td>
                    <div class="cell">92274.1</div>
                  </td>
                  <td>
                    <div class="cell">5483.4</div>
                  </td>
                  <td>
                    <div class="cell">27%</div>
                  </td>
                  <td>
                    <div class="cell">151.3%</div>
                  </td>
                  <td>
                    <div class="cell">38256.8</div>
                  </td>
                  <td>
                    <div class="cell">2009.7</div>
                  </td>
                  <td>
                    <div class="cell">11.4%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">4.9%</div>
                  </td>
                  <td>
                    <div class="cell">66%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:13</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">12</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5cd022c1258f158b76b9856a9fb52389.png" alt="Fly" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Fly</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">69</div>
                  </td>
                  <td>
                    <div class="cell">47</div>
                  </td>
                  <td>
                    <div class="cell">68.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">1.9 / 1.7 / 4.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">4.7</div>
                  </td>
                  <td>
                    <div class="cell">9333.5</div>
                  </td>
                  <td>
                    <div class="cell">591.2</div>
                  </td>
                  <td>
                    <div class="cell">19%</div>
                  </td>
                  <td>
                    <div class="cell">53718</div>
                  </td>
                  <td>
                    <div class="cell">3201.7</div>
                  </td>
                  <td>
                    <div class="cell">15.9%</div>
                  </td>
                  <td>
                    <div class="cell">83.6%</div>
                  </td>
                  <td>
                    <div class="cell">92917.1</div>
                  </td>
                  <td>
                    <div class="cell">4485.6</div>
                  </td>
                  <td>
                    <div class="cell">26%</div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">17.8%</div>
                  </td>
                  <td>
                    <div class="cell">59.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:29</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">13</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/36ee63cce8a0061c6c2d887f2ebbe622.png" alt="一笙" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">一笙</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">15</div>
                  </td>
                  <td>
                    <div class="cell">10</div>
                  </td>
                  <td>
                    <div class="cell">66.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">6.3</span>
                      <span class="kda2">0.9 / 1.5 / 7.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.9</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">7.8</div>
                  </td>
                  <td>
                    <div class="cell">7272.8</div>
                  </td>
                  <td>
                    <div class="cell">448.8</div>
                  </td>
                  <td>
                    <div class="cell">14.6%</div>
                  </td>
                  <td>
                    <div class="cell">34947.3</div>
                  </td>
                  <td>
                    <div class="cell">1997.5</div>
                  </td>
                  <td>
                    <div class="cell">10.2%</div>
                  </td>
                  <td>
                    <div class="cell">70.1%</div>
                  </td>
                  <td>
                    <div class="cell">92714</div>
                  </td>
                  <td>
                    <div class="cell">4731.2</div>
                  </td>
                  <td>
                    <div class="cell">24.8%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0.7%</div>
                  </td>
                  <td>
                    <div class="cell">85.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">14</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/34b847d9d4acf1fb377d2b4fd50af251.png" alt="誓约" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">誓约</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">29</div>
                  </td>
                  <td>
                    <div class="cell">18</div>
                  </td>
                  <td>
                    <div class="cell">62%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4</span>
                      <span class="kda2">2.1 / 2 / 3.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">3.8</div>
                  </td>
                  <td>
                    <div class="cell">9791.5</div>
                  </td>
                  <td>
                    <div class="cell">620.3</div>
                  </td>
                  <td>
                    <div class="cell">19.9%</div>
                  </td>
                  <td>
                    <div class="cell">44036.7</div>
                  </td>
                  <td>
                    <div class="cell">2672.7</div>
                  </td>
                  <td>
                    <div class="cell">15.6%</div>
                  </td>
                  <td>
                    <div class="cell">79.5%</div>
                  </td>
                  <td>
                    <div class="cell">85698.4</div>
                  </td>
                  <td>
                    <div class="cell">4263.1</div>
                  </td>
                  <td>
                    <div class="cell">23.9%</div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">13.4%</div>
                  </td>
                  <td>
                    <div class="cell">68.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:29</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">15</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2a4ea3d4cca408009c033f13509ed748.png" alt="一门" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">一门</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">17</div>
                  </td>
                  <td>
                    <div class="cell">10</div>
                  </td>
                  <td>
                    <div class="cell">58.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">6.7</span>
                      <span class="kda2">0.6 / 1.2 / 7.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">7.2</div>
                  </td>
                  <td>
                    <div class="cell">7622.2</div>
                  </td>
                  <td>
                    <div class="cell">483.6</div>
                  </td>
                  <td>
                    <div class="cell">15.2%</div>
                  </td>
                  <td>
                    <div class="cell">26492.1</div>
                  </td>
                  <td>
                    <div class="cell">1567.5</div>
                  </td>
                  <td>
                    <div class="cell">8.9%</div>
                  </td>
                  <td>
                    <div class="cell">58.4%</div>
                  </td>
                  <td>
                    <div class="cell">79300.3</div>
                  </td>
                  <td>
                    <div class="cell">3947.8</div>
                  </td>
                  <td>
                    <div class="cell">24.4%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0.7%</div>
                  </td>
                  <td>
                    <div class="cell">82.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:33</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">16</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/b762a5abeaa00cd1da6fdd77c490161b.png" alt="暖阳（林恒）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">暖阳（林恒）</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">81</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">56.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.4</span>
                      <span class="kda2">2.8 / 1.9 / 4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.8</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">12184.8</div>
                  </td>
                  <td>
                    <div class="cell">740</div>
                  </td>
                  <td>
                    <div class="cell">23.6%</div>
                  </td>
                  <td>
                    <div class="cell">55187.9</div>
                  </td>
                  <td>
                    <div class="cell">3135.1</div>
                  </td>
                  <td>
                    <div class="cell">17.7%</div>
                  </td>
                  <td>
                    <div class="cell">75.5%</div>
                  </td>
                  <td>
                    <div class="cell">93275.3</div>
                  </td>
                  <td>
                    <div class="cell">3787.7</div>
                  </td>
                  <td>
                    <div class="cell">21%</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">15.9%</div>
                  </td>
                  <td>
                    <div class="cell">67.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">17</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8d45528e4577c5ecb17f2aa37a78dde4.png" alt="梓墨" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">梓墨</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">81</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">56.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.5</span>
                      <span class="kda2">1.7 / 1.8 / 4.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">4.7</div>
                  </td>
                  <td>
                    <div class="cell">9598.9</div>
                  </td>
                  <td>
                    <div class="cell">584.1</div>
                  </td>
                  <td>
                    <div class="cell">18.8%</div>
                  </td>
                  <td>
                    <div class="cell">51998.2</div>
                  </td>
                  <td>
                    <div class="cell">3007.6</div>
                  </td>
                  <td>
                    <div class="cell">17.2%</div>
                  </td>
                  <td>
                    <div class="cell">92.8%</div>
                  </td>
                  <td>
                    <div class="cell">102158.2</div>
                  </td>
                  <td>
                    <div class="cell">4897.5</div>
                  </td>
                  <td>
                    <div class="cell">27.7%</div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">14%</div>
                  </td>
                  <td>
                    <div class="cell">61.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">18</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/6031efec47f5ad279253f962635a0ecc.png" alt="星宇" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">星宇</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">81</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">56.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.9</span>
                      <span class="kda2">0.5 / 1.4 / 7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">7</div>
                  </td>
                  <td>
                    <div class="cell">7515.7</div>
                  </td>
                  <td>
                    <div class="cell">458.1</div>
                  </td>
                  <td>
                    <div class="cell">14.7%</div>
                  </td>
                  <td>
                    <div class="cell">24288.2</div>
                  </td>
                  <td>
                    <div class="cell">1440.6</div>
                  </td>
                  <td>
                    <div class="cell">8.2%</div>
                  </td>
                  <td>
                    <div class="cell">56.1%</div>
                  </td>
                  <td>
                    <div class="cell">85062.3</div>
                  </td>
                  <td>
                    <div class="cell">4222.7</div>
                  </td>
                  <td>
                    <div class="cell">23.3%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2.8%</div>
                  </td>
                  <td>
                    <div class="cell">74.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">19</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/14541912d6728e93c66a42a23bf32cfe.png" alt="花卷" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">花卷</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">81</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">56.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.2</span>
                      <span class="kda2">2 / 1.5 / 4.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">4.9</div>
                  </td>
                  <td>
                    <div class="cell">9345.4</div>
                  </td>
                  <td>
                    <div class="cell">563.9</div>
                  </td>
                  <td>
                    <div class="cell">18.1%</div>
                  </td>
                  <td>
                    <div class="cell">88657.4</div>
                  </td>
                  <td>
                    <div class="cell">5068.8</div>
                  </td>
                  <td>
                    <div class="cell">28.7%</div>
                  </td>
                  <td>
                    <div class="cell">157.8%</div>
                  </td>
                  <td>
                    <div class="cell">43114.5</div>
                  </td>
                  <td>
                    <div class="cell">2173.3</div>
                  </td>
                  <td>
                    <div class="cell">12.1%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2.3%</div>
                  </td>
                  <td>
                    <div class="cell">70.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">20</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2109f8770f35fe7af93e8e2866bb393d.png" alt="乔兮" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">乔兮</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">81</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">56.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">2.8 / 1.6 / 3.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.8</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">3.9</div>
                  </td>
                  <td>
                    <div class="cell">12617.8</div>
                  </td>
                  <td>
                    <div class="cell">766.7</div>
                  </td>
                  <td>
                    <div class="cell">24.6%</div>
                  </td>
                  <td>
                    <div class="cell">86342.6</div>
                  </td>
                  <td>
                    <div class="cell">4872.9</div>
                  </td>
                  <td>
                    <div class="cell">27.9%</div>
                  </td>
                  <td>
                    <div class="cell">113%</div>
                  </td>
                  <td>
                    <div class="cell">62626.5</div>
                  </td>
                  <td>
                    <div class="cell">2779.3</div>
                  </td>
                  <td>
                    <div class="cell">15.6%</div>
                  </td>
                  <td>
                    <div class="cell">2.6</div>
                  </td>
                  <td>
                    <div class="cell">42.7%</div>
                  </td>
                  <td>
                    <div class="cell">64.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">21</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ce86be8444a4587fd6a5201d2a1fb4ed.png" alt="不然" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">不然</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">71</div>
                  </td>
                  <td>
                    <div class="cell">40</div>
                  </td>
                  <td>
                    <div class="cell">56.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">3.2 / 1.7 / 4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3.2</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">12731.4</div>
                  </td>
                  <td>
                    <div class="cell">782.8</div>
                  </td>
                  <td>
                    <div class="cell">24.9%</div>
                  </td>
                  <td>
                    <div class="cell">51794.2</div>
                  </td>
                  <td>
                    <div class="cell">3035.3</div>
                  </td>
                  <td>
                    <div class="cell">16.9%</div>
                  </td>
                  <td>
                    <div class="cell">68.3%</div>
                  </td>
                  <td>
                    <div class="cell">83303.9</div>
                  </td>
                  <td>
                    <div class="cell">3347.4</div>
                  </td>
                  <td>
                    <div class="cell">20%</div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">12%</div>
                  </td>
                  <td>
                    <div class="cell">69%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">22</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/eb48fec336a3035bbaff57bda95d65c5.png" alt="阿豆（蒋涛）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">阿豆（蒋涛）</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">71</div>
                  </td>
                  <td>
                    <div class="cell">40</div>
                  </td>
                  <td>
                    <div class="cell">56.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.8</span>
                      <span class="kda2">0.5 / 1.7 / 7.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">7.5</div>
                  </td>
                  <td>
                    <div class="cell">7261.1</div>
                  </td>
                  <td>
                    <div class="cell">448</div>
                  </td>
                  <td>
                    <div class="cell">14.2%</div>
                  </td>
                  <td>
                    <div class="cell">32722.9</div>
                  </td>
                  <td>
                    <div class="cell">1838.2</div>
                  </td>
                  <td>
                    <div class="cell">10.1%</div>
                  </td>
                  <td>
                    <div class="cell">71%</div>
                  </td>
                  <td>
                    <div class="cell">75589.7</div>
                  </td>
                  <td>
                    <div class="cell">3818</div>
                  </td>
                  <td>
                    <div class="cell">22.5%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">1.2%</div>
                  </td>
                  <td>
                    <div class="cell">75%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">23</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/cd3b48b9f8fe8e96abab73573cd83965.png" alt="风箫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">风箫</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">71</div>
                  </td>
                  <td>
                    <div class="cell">40</div>
                  </td>
                  <td>
                    <div class="cell">56.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.3</span>
                      <span class="kda2">2.5 / 2.1 / 4.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">4.2</div>
                  </td>
                  <td>
                    <div class="cell">12308.9</div>
                  </td>
                  <td>
                    <div class="cell">753.3</div>
                  </td>
                  <td>
                    <div class="cell">24%</div>
                  </td>
                  <td>
                    <div class="cell">90852.2</div>
                  </td>
                  <td>
                    <div class="cell">5190.3</div>
                  </td>
                  <td>
                    <div class="cell">28.6%</div>
                  </td>
                  <td>
                    <div class="cell">118.8%</div>
                  </td>
                  <td>
                    <div class="cell">64742.3</div>
                  </td>
                  <td>
                    <div class="cell">2921.6</div>
                  </td>
                  <td>
                    <div class="cell">17.6%</div>
                  </td>
                  <td>
                    <div class="cell">2.6</div>
                  </td>
                  <td>
                    <div class="cell">40.6%</div>
                  </td>
                  <td>
                    <div class="cell">64.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">24</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/42c878fddfd0d188f155b6c497e0c5c8.png" alt="清清" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">清清</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">71</div>
                  </td>
                  <td>
                    <div class="cell">40</div>
                  </td>
                  <td>
                    <div class="cell">56.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">2.2 / 1.7 / 4.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">4.9</div>
                  </td>
                  <td>
                    <div class="cell">9600.8</div>
                  </td>
                  <td>
                    <div class="cell">587.9</div>
                  </td>
                  <td>
                    <div class="cell">18.7%</div>
                  </td>
                  <td>
                    <div class="cell">52293.7</div>
                  </td>
                  <td>
                    <div class="cell">3049.2</div>
                  </td>
                  <td>
                    <div class="cell">17%</div>
                  </td>
                  <td>
                    <div class="cell">91.3%</div>
                  </td>
                  <td>
                    <div class="cell">94515.6</div>
                  </td>
                  <td>
                    <div class="cell">4625.2</div>
                  </td>
                  <td>
                    <div class="cell">27.6%</div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">13.6%</div>
                  </td>
                  <td>
                    <div class="cell">68.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">25</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/6d899f90a771b5aef541a5c548363764.png" alt="九尾" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">九尾</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">71</div>
                  </td>
                  <td>
                    <div class="cell">40</div>
                  </td>
                  <td>
                    <div class="cell">56.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.4</span>
                      <span class="kda2">1.7 / 1.5 / 5.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">5.4</div>
                  </td>
                  <td>
                    <div class="cell">9142.1</div>
                  </td>
                  <td>
                    <div class="cell">563.6</div>
                  </td>
                  <td>
                    <div class="cell">18%</div>
                  </td>
                  <td>
                    <div class="cell">84601.6</div>
                  </td>
                  <td>
                    <div class="cell">4952.3</div>
                  </td>
                  <td>
                    <div class="cell">27.1%</div>
                  </td>
                  <td>
                    <div class="cell">150.7%</div>
                  </td>
                  <td>
                    <div class="cell">40878.7</div>
                  </td>
                  <td>
                    <div class="cell">2058.9</div>
                  </td>
                  <td>
                    <div class="cell">12%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">3.7%</div>
                  </td>
                  <td>
                    <div class="cell">69%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">26</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5933ec732ac62f3a76813239d4217ae4.png" alt="早点" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">早点</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">87</div>
                  </td>
                  <td>
                    <div class="cell">48</div>
                  </td>
                  <td>
                    <div class="cell">55.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.5</span>
                      <span class="kda2">1.4 / 1.2 / 5.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">5.3</div>
                  </td>
                  <td>
                    <div class="cell">8944</div>
                  </td>
                  <td>
                    <div class="cell">536.6</div>
                  </td>
                  <td>
                    <div class="cell">17.5%</div>
                  </td>
                  <td>
                    <div class="cell">97258.9</div>
                  </td>
                  <td>
                    <div class="cell">5396</div>
                  </td>
                  <td>
                    <div class="cell">28.9%</div>
                  </td>
                  <td>
                    <div class="cell">163.8%</div>
                  </td>
                  <td>
                    <div class="cell">40811.8</div>
                  </td>
                  <td>
                    <div class="cell">2015</div>
                  </td>
                  <td>
                    <div class="cell">11%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">3%</div>
                  </td>
                  <td>
                    <div class="cell">70.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:20</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">27</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/e1906088d0ae9e9d2c0c2ae4933748fd.png" alt="未央" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">未央</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">53</div>
                  </td>
                  <td>
                    <div class="cell">29</div>
                  </td>
                  <td>
                    <div class="cell">54.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">2.3 / 1.7 / 3.1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.3</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">3.1</div>
                  </td>
                  <td>
                    <div class="cell">11551.7</div>
                  </td>
                  <td>
                    <div class="cell">723.7</div>
                  </td>
                  <td>
                    <div class="cell">23.1%</div>
                  </td>
                  <td>
                    <div class="cell">44780.9</div>
                  </td>
                  <td>
                    <div class="cell">2686.6</div>
                  </td>
                  <td>
                    <div class="cell">15.6%</div>
                  </td>
                  <td>
                    <div class="cell">68.8%</div>
                  </td>
                  <td>
                    <div class="cell">80753.7</div>
                  </td>
                  <td>
                    <div class="cell">3395.4</div>
                  </td>
                  <td>
                    <div class="cell">20.3%</div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">10.8%</div>
                  </td>
                  <td>
                    <div class="cell">64.9%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">28</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/c887c33254a27e4b6990f4c52f33d9df.png" alt="Cat" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Cat</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">85</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">54.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.3</span>
                      <span class="kda2">0.4 / 2.2 / 6.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.4</div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">6.4</div>
                  </td>
                  <td>
                    <div class="cell">7336.2</div>
                  </td>
                  <td>
                    <div class="cell">440.6</div>
                  </td>
                  <td>
                    <div class="cell">14.4%</div>
                  </td>
                  <td>
                    <div class="cell">28751.5</div>
                  </td>
                  <td>
                    <div class="cell">1629.8</div>
                  </td>
                  <td>
                    <div class="cell">8.9%</div>
                  </td>
                  <td>
                    <div class="cell">62.2%</div>
                  </td>
                  <td>
                    <div class="cell">95358.4</div>
                  </td>
                  <td>
                    <div class="cell">4800.7</div>
                  </td>
                  <td>
                    <div class="cell">26.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2.5%</div>
                  </td>
                  <td>
                    <div class="cell">75.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:18</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">29</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/1dc617e6ee4edc26f834b370dd0fb879.png" alt="绝意" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">绝意</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">85</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">54.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.2</span>
                      <span class="kda2">2.9 / 1.7 / 3.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.9</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">3.4</div>
                  </td>
                  <td>
                    <div class="cell">12438</div>
                  </td>
                  <td>
                    <div class="cell">747</div>
                  </td>
                  <td>
                    <div class="cell">24.4%</div>
                  </td>
                  <td>
                    <div class="cell">88220.9</div>
                  </td>
                  <td>
                    <div class="cell">4924.6</div>
                  </td>
                  <td>
                    <div class="cell">26.7%</div>
                  </td>
                  <td>
                    <div class="cell">108.4%</div>
                  </td>
                  <td>
                    <div class="cell">60284.1</div>
                  </td>
                  <td>
                    <div class="cell">2620.8</div>
                  </td>
                  <td>
                    <div class="cell">14.5%</div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">40.9%</div>
                  </td>
                  <td>
                    <div class="cell">68.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:16</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">30</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8bc3ee8cf44809ac7f6cf9f3db18bfbd.png" alt="赤辰" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">赤辰</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">89</div>
                  </td>
                  <td>
                    <div class="cell">48</div>
                  </td>
                  <td>
                    <div class="cell">53.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.8</span>
                      <span class="kda2">1.9 / 2 / 4.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">4.2</div>
                  </td>
                  <td>
                    <div class="cell">11582.8</div>
                  </td>
                  <td>
                    <div class="cell">696.3</div>
                  </td>
                  <td>
                    <div class="cell">22.7%</div>
                  </td>
                  <td>
                    <div class="cell">53945.2</div>
                  </td>
                  <td>
                    <div class="cell">3113.4</div>
                  </td>
                  <td>
                    <div class="cell">17.2%</div>
                  </td>
                  <td>
                    <div class="cell">76.3%</div>
                  </td>
                  <td>
                    <div class="cell">98703.7</div>
                  </td>
                  <td>
                    <div class="cell">4235.2</div>
                  </td>
                  <td>
                    <div class="cell">24%</div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">15.2%</div>
                  </td>
                  <td>
                    <div class="cell">64.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:15</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">31</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a9d72875be343eaa9ece04de5c15c04d.png" alt="小落" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小落</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">89</div>
                  </td>
                  <td>
                    <div class="cell">48</div>
                  </td>
                  <td>
                    <div class="cell">53.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2.2 / 2.1 / 4.1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">4.1</div>
                  </td>
                  <td>
                    <div class="cell">10475.5</div>
                  </td>
                  <td>
                    <div class="cell">634.2</div>
                  </td>
                  <td>
                    <div class="cell">20.7%</div>
                  </td>
                  <td>
                    <div class="cell">57812.1</div>
                  </td>
                  <td>
                    <div class="cell">3309.5</div>
                  </td>
                  <td>
                    <div class="cell">18.2%</div>
                  </td>
                  <td>
                    <div class="cell">87.9%</div>
                  </td>
                  <td>
                    <div class="cell">92309.9</div>
                  </td>
                  <td>
                    <div class="cell">4358.7</div>
                  </td>
                  <td>
                    <div class="cell">24.2%</div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">17.7%</div>
                  </td>
                  <td>
                    <div class="cell">69.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:15</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">32</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/47426b6d08ba1b9eb5d9ae750dba2e1d.png" alt="清融" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">清融</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">78</div>
                  </td>
                  <td>
                    <div class="cell">42</div>
                  </td>
                  <td>
                    <div class="cell">53.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.8</span>
                      <span class="kda2">2.1 / 1.8 / 6.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">6.2</div>
                  </td>
                  <td>
                    <div class="cell">9154.6</div>
                  </td>
                  <td>
                    <div class="cell">561.1</div>
                  </td>
                  <td>
                    <div class="cell">18.1%</div>
                  </td>
                  <td>
                    <div class="cell">100653.8</div>
                  </td>
                  <td>
                    <div class="cell">5842.1</div>
                  </td>
                  <td>
                    <div class="cell">30.5%</div>
                  </td>
                  <td>
                    <div class="cell">168%</div>
                  </td>
                  <td>
                    <div class="cell">48426.2</div>
                  </td>
                  <td>
                    <div class="cell">2435.8</div>
                  </td>
                  <td>
                    <div class="cell">14.2%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">4%</div>
                  </td>
                  <td>
                    <div class="cell">74.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">33</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fabf19fb0188947220f55e0a309fe101.png" alt="子阳" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">子阳</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">78</div>
                  </td>
                  <td>
                    <div class="cell">42</div>
                  </td>
                  <td>
                    <div class="cell">53.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">6.6</span>
                      <span class="kda2">0.7 / 1.7 / 8.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">8.3</div>
                  </td>
                  <td>
                    <div class="cell">7243.8</div>
                  </td>
                  <td>
                    <div class="cell">442.5</div>
                  </td>
                  <td>
                    <div class="cell">14.3%</div>
                  </td>
                  <td>
                    <div class="cell">32841.9</div>
                  </td>
                  <td>
                    <div class="cell">1869.1</div>
                  </td>
                  <td>
                    <div class="cell">9.7%</div>
                  </td>
                  <td>
                    <div class="cell">67.5%</div>
                  </td>
                  <td>
                    <div class="cell">65748.6</div>
                  </td>
                  <td>
                    <div class="cell">3362.2</div>
                  </td>
                  <td>
                    <div class="cell">19.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">1.6%</div>
                  </td>
                  <td>
                    <div class="cell">80.1%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">34</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/11872ff2e53bc3fc33d028cc9daf749d.png" alt="花海（罗思源）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">花海（罗思源）</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">78</div>
                  </td>
                  <td>
                    <div class="cell">42</div>
                  </td>
                  <td>
                    <div class="cell">53.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.1</span>
                      <span class="kda2">3.3 / 2 / 4.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3.3</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">4.6</div>
                  </td>
                  <td>
                    <div class="cell">12672.8</div>
                  </td>
                  <td>
                    <div class="cell">774.5</div>
                  </td>
                  <td>
                    <div class="cell">25.1%</div>
                  </td>
                  <td>
                    <div class="cell">55614.6</div>
                  </td>
                  <td>
                    <div class="cell">3303.2</div>
                  </td>
                  <td>
                    <div class="cell">17.4%</div>
                  </td>
                  <td>
                    <div class="cell">70.2%</div>
                  </td>
                  <td>
                    <div class="cell">89348.1</div>
                  </td>
                  <td>
                    <div class="cell">3706.6</div>
                  </td>
                  <td>
                    <div class="cell">21.8%</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">15.4%</div>
                  </td>
                  <td>
                    <div class="cell">70.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">35</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ade9f2ceee080e3d63dad74b30d252d6.png" alt="坦然（孙麟威）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">坦然（孙麟威）</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">78</div>
                  </td>
                  <td>
                    <div class="cell">42</div>
                  </td>
                  <td>
                    <div class="cell">53.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">1.9 / 1.9 / 5.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">5.6</div>
                  </td>
                  <td>
                    <div class="cell">9101.1</div>
                  </td>
                  <td>
                    <div class="cell">565.2</div>
                  </td>
                  <td>
                    <div class="cell">18.2%</div>
                  </td>
                  <td>
                    <div class="cell">49505.5</div>
                  </td>
                  <td>
                    <div class="cell">2969.8</div>
                  </td>
                  <td>
                    <div class="cell">15.7%</div>
                  </td>
                  <td>
                    <div class="cell">85.9%</div>
                  </td>
                  <td>
                    <div class="cell">95057.3</div>
                  </td>
                  <td>
                    <div class="cell">4675</div>
                  </td>
                  <td>
                    <div class="cell">27.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">11.6%</div>
                  </td>
                  <td>
                    <div class="cell">66.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">36</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/f6bfc9197e6dc0dfe8ffcac26544c8b8.png" alt="言梦" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">言梦</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">15</div>
                  </td>
                  <td>
                    <div class="cell">53.5%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.4</span>
                      <span class="kda2">0.5 / 1.8 / 7.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">7.2</div>
                  </td>
                  <td>
                    <div class="cell">6949.6</div>
                  </td>
                  <td>
                    <div class="cell">414.3</div>
                  </td>
                  <td>
                    <div class="cell">13.4%</div>
                  </td>
                  <td>
                    <div class="cell">31599.2</div>
                  </td>
                  <td>
                    <div class="cell">1789.3</div>
                  </td>
                  <td>
                    <div class="cell">10.1%</div>
                  </td>
                  <td>
                    <div class="cell">76.2%</div>
                  </td>
                  <td>
                    <div class="cell">83913.9</div>
                  </td>
                  <td>
                    <div class="cell">4256.9</div>
                  </td>
                  <td>
                    <div class="cell">24%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">5.6%</div>
                  </td>
                  <td>
                    <div class="cell">77.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">37</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5ce064c461a25bc1594d17a707e975a4.png" alt="今屿" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">今屿</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">45</div>
                  </td>
                  <td>
                    <div class="cell">24</div>
                  </td>
                  <td>
                    <div class="cell">53.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.6</span>
                      <span class="kda2">2.4 / 1.8 / 3.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">3.9</div>
                  </td>
                  <td>
                    <div class="cell">12610.5</div>
                  </td>
                  <td>
                    <div class="cell">775</div>
                  </td>
                  <td>
                    <div class="cell">25.2%</div>
                  </td>
                  <td>
                    <div class="cell">57800.3</div>
                  </td>
                  <td>
                    <div class="cell">3322.1</div>
                  </td>
                  <td>
                    <div class="cell">19%</div>
                  </td>
                  <td>
                    <div class="cell">76.4%</div>
                  </td>
                  <td>
                    <div class="cell">94098.7</div>
                  </td>
                  <td>
                    <div class="cell">3853.2</div>
                  </td>
                  <td>
                    <div class="cell">21.5%</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">18.8%</div>
                  </td>
                  <td>
                    <div class="cell">67.9%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:02</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">38</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d650a1c4a421465ea1324f85691432cd.png" alt="傲寒" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">傲寒</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">77</div>
                  </td>
                  <td>
                    <div class="cell">41</div>
                  </td>
                  <td>
                    <div class="cell">53.2%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2.4 / 1.9 / 3.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">3.7</div>
                  </td>
                  <td>
                    <div class="cell">12076.8</div>
                  </td>
                  <td>
                    <div class="cell">755.3</div>
                  </td>
                  <td>
                    <div class="cell">24.5%</div>
                  </td>
                  <td>
                    <div class="cell">85885.6</div>
                  </td>
                  <td>
                    <div class="cell">5049.2</div>
                  </td>
                  <td>
                    <div class="cell">28%</div>
                  </td>
                  <td>
                    <div class="cell">112.5%</div>
                  </td>
                  <td>
                    <div class="cell">58655.4</div>
                  </td>
                  <td>
                    <div class="cell">2657.3</div>
                  </td>
                  <td>
                    <div class="cell">14.7%</div>
                  </td>
                  <td>
                    <div class="cell">2.8</div>
                  </td>
                  <td>
                    <div class="cell">47.5%</div>
                  </td>
                  <td>
                    <div class="cell">66.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:15</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">39</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/c9bd1afee0b367315b98a831f1389c99.png" alt="铃铛" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">铃铛</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">47</div>
                  </td>
                  <td>
                    <div class="cell">25</div>
                  </td>
                  <td>
                    <div class="cell">53.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.5</span>
                      <span class="kda2">1.5 / 1.3 / 4.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">4.4</div>
                  </td>
                  <td>
                    <div class="cell">9489.4</div>
                  </td>
                  <td>
                    <div class="cell">608.6</div>
                  </td>
                  <td>
                    <div class="cell">19.8%</div>
                  </td>
                  <td>
                    <div class="cell">94245.5</div>
                  </td>
                  <td>
                    <div class="cell">5577.6</div>
                  </td>
                  <td>
                    <div class="cell">31%</div>
                  </td>
                  <td>
                    <div class="cell">159.2%</div>
                  </td>
                  <td>
                    <div class="cell">42293.4</div>
                  </td>
                  <td>
                    <div class="cell">2178.9</div>
                  </td>
                  <td>
                    <div class="cell">11.8%</div>
                  </td>
                  <td>
                    <div class="cell">0.9</div>
                  </td>
                  <td>
                    <div class="cell">18.4%</div>
                  </td>
                  <td>
                    <div class="cell">69.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:19</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">40</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9573fcc4b7d8805532f762ed6785edaa.png" alt="鹏鹏" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">鹏鹏</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">91</div>
                  </td>
                  <td>
                    <div class="cell">48</div>
                  </td>
                  <td>
                    <div class="cell">52.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2.5 / 1.9 / 3.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">3.5</div>
                  </td>
                  <td>
                    <div class="cell">12071.6</div>
                  </td>
                  <td>
                    <div class="cell">730.8</div>
                  </td>
                  <td>
                    <div class="cell">23.6%</div>
                  </td>
                  <td>
                    <div class="cell">49479.5</div>
                  </td>
                  <td>
                    <div class="cell">2847.1</div>
                  </td>
                  <td>
                    <div class="cell">17.2%</div>
                  </td>
                  <td>
                    <div class="cell">72.7%</div>
                  </td>
                  <td>
                    <div class="cell">90862.1</div>
                  </td>
                  <td>
                    <div class="cell">3734.4</div>
                  </td>
                  <td>
                    <div class="cell">22.1%</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">20.5%</div>
                  </td>
                  <td>
                    <div class="cell">68.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">41</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/faac4faa28d92bddc3e143afdd057921.png" alt="阿改" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">阿改</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">91</div>
                  </td>
                  <td>
                    <div class="cell">48</div>
                  </td>
                  <td>
                    <div class="cell">52.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.4</span>
                      <span class="kda2">0.6 / 1.4 / 6.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">6.3</div>
                  </td>
                  <td>
                    <div class="cell">7505.1</div>
                  </td>
                  <td>
                    <div class="cell">454.7</div>
                  </td>
                  <td>
                    <div class="cell">14.7%</div>
                  </td>
                  <td>
                    <div class="cell">26501.5</div>
                  </td>
                  <td>
                    <div class="cell">1503.6</div>
                  </td>
                  <td>
                    <div class="cell">8.8%</div>
                  </td>
                  <td>
                    <div class="cell">59.8%</div>
                  </td>
                  <td>
                    <div class="cell">70767.4</div>
                  </td>
                  <td>
                    <div class="cell">3612.9</div>
                  </td>
                  <td>
                    <div class="cell">20.8%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">5.1%</div>
                  </td>
                  <td>
                    <div class="cell">79.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">42</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/03d1c607fdee6e1f4526d9568ae165d8.png" alt="青枫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">青枫</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">91</div>
                  </td>
                  <td>
                    <div class="cell">48</div>
                  </td>
                  <td>
                    <div class="cell">52.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">1.5 / 1.4 / 4.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">4.7</div>
                  </td>
                  <td>
                    <div class="cell">9083.8</div>
                  </td>
                  <td>
                    <div class="cell">548.5</div>
                  </td>
                  <td>
                    <div class="cell">17.7%</div>
                  </td>
                  <td>
                    <div class="cell">85344.4</div>
                  </td>
                  <td>
                    <div class="cell">4866.2</div>
                  </td>
                  <td>
                    <div class="cell">28.9%</div>
                  </td>
                  <td>
                    <div class="cell">161.1%</div>
                  </td>
                  <td>
                    <div class="cell">43714.6</div>
                  </td>
                  <td>
                    <div class="cell">2241.6</div>
                  </td>
                  <td>
                    <div class="cell">13.1%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">3.4%</div>
                  </td>
                  <td>
                    <div class="cell">69.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">43</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/37f7d0359012b5e38e44202f686f271e.png" alt="百兽" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">百兽</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">91</div>
                  </td>
                  <td>
                    <div class="cell">48</div>
                  </td>
                  <td>
                    <div class="cell">52.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">1.3 / 1.9 / 4.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">4.4</div>
                  </td>
                  <td>
                    <div class="cell">9178.6</div>
                  </td>
                  <td>
                    <div class="cell">557.7</div>
                  </td>
                  <td>
                    <div class="cell">18.1%</div>
                  </td>
                  <td>
                    <div class="cell">39553</div>
                  </td>
                  <td>
                    <div class="cell">2296.6</div>
                  </td>
                  <td>
                    <div class="cell">13.7%</div>
                  </td>
                  <td>
                    <div class="cell">75%</div>
                  </td>
                  <td>
                    <div class="cell">90759.7</div>
                  </td>
                  <td>
                    <div class="cell">4459.7</div>
                  </td>
                  <td>
                    <div class="cell">26.3%</div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">13.1%</div>
                  </td>
                  <td>
                    <div class="cell">65.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">44</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9e2b874427ddb2f23452748c340b266a.png" alt="梦岚" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">梦岚</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">91</div>
                  </td>
                  <td>
                    <div class="cell">48</div>
                  </td>
                  <td>
                    <div class="cell">52.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">2.5 / 1.6 / 3.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">3.9</div>
                  </td>
                  <td>
                    <div class="cell">12567.7</div>
                  </td>
                  <td>
                    <div class="cell">760</div>
                  </td>
                  <td>
                    <div class="cell">24.6%</div>
                  </td>
                  <td>
                    <div class="cell">87991.1</div>
                  </td>
                  <td>
                    <div class="cell">5021.2</div>
                  </td>
                  <td>
                    <div class="cell">30.1%</div>
                  </td>
                  <td>
                    <div class="cell">120.5%</div>
                  </td>
                  <td>
                    <div class="cell">62877.7</div>
                  </td>
                  <td>
                    <div class="cell">2775</div>
                  </td>
                  <td>
                    <div class="cell">16.3%</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">30.4%</div>
                  </td>
                  <td>
                    <div class="cell">73.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">45</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/f50df692e9332268fc0461bc15dc09fb.png" alt="易峥" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">易峥</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">73</div>
                  </td>
                  <td>
                    <div class="cell">38</div>
                  </td>
                  <td>
                    <div class="cell">52%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5</span>
                      <span class="kda2">2.9 / 2 / 4.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.9</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">4.8</div>
                  </td>
                  <td>
                    <div class="cell">12098.6</div>
                  </td>
                  <td>
                    <div class="cell">742.9</div>
                  </td>
                  <td>
                    <div class="cell">24%</div>
                  </td>
                  <td>
                    <div class="cell">88326.6</div>
                  </td>
                  <td>
                    <div class="cell">5023.2</div>
                  </td>
                  <td>
                    <div class="cell">26.5%</div>
                  </td>
                  <td>
                    <div class="cell">109.4%</div>
                  </td>
                  <td>
                    <div class="cell">63834</div>
                  </td>
                  <td>
                    <div class="cell">2841.9</div>
                  </td>
                  <td>
                    <div class="cell">16.7%</div>
                  </td>
                  <td>
                    <div class="cell">3.1</div>
                  </td>
                  <td>
                    <div class="cell">50.4%</div>
                  </td>
                  <td>
                    <div class="cell">70.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">46</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0588a8dd00258118b5cf1fcb610556af.png" alt="无畏" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">无畏</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">89</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">51.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">1.8 / 1.9 / 3.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">3.6</div>
                  </td>
                  <td>
                    <div class="cell">11187.3</div>
                  </td>
                  <td>
                    <div class="cell">709.4</div>
                  </td>
                  <td>
                    <div class="cell">23%</div>
                  </td>
                  <td>
                    <div class="cell">52654</div>
                  </td>
                  <td>
                    <div class="cell">3125.8</div>
                  </td>
                  <td>
                    <div class="cell">17.5%</div>
                  </td>
                  <td>
                    <div class="cell">76.5%</div>
                  </td>
                  <td>
                    <div class="cell">94422.9</div>
                  </td>
                  <td>
                    <div class="cell">4259.3</div>
                  </td>
                  <td>
                    <div class="cell">24%</div>
                  </td>
                  <td>
                    <div class="cell">0.9</div>
                  </td>
                  <td>
                    <div class="cell">14.6%</div>
                  </td>
                  <td>
                    <div class="cell">62.1%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:04</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">47</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0bc827584405baaceb878f98453ff248.png" alt="玄影" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">玄影</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">43</div>
                  </td>
                  <td>
                    <div class="cell">22</div>
                  </td>
                  <td>
                    <div class="cell">51.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">2.2 / 2.1 / 3.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">3.6</div>
                  </td>
                  <td>
                    <div class="cell">12667.9</div>
                  </td>
                  <td>
                    <div class="cell">774.5</div>
                  </td>
                  <td>
                    <div class="cell">24.8%</div>
                  </td>
                  <td>
                    <div class="cell">47321.7</div>
                  </td>
                  <td>
                    <div class="cell">2701.6</div>
                  </td>
                  <td>
                    <div class="cell">15.4%</div>
                  </td>
                  <td>
                    <div class="cell">63%</div>
                  </td>
                  <td>
                    <div class="cell">82429.8</div>
                  </td>
                  <td>
                    <div class="cell">3281.3</div>
                  </td>
                  <td>
                    <div class="cell">18.4%</div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">24.8%</div>
                  </td>
                  <td>
                    <div class="cell">57.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">48</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d6d8526e6342b92e8d01233ccbd5df94.png" alt="Roc" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Roc</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">43</div>
                  </td>
                  <td>
                    <div class="cell">22</div>
                  </td>
                  <td>
                    <div class="cell">51.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.6</span>
                      <span class="kda2">3 / 1.7 / 3.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">3.5</div>
                  </td>
                  <td>
                    <div class="cell">12799.4</div>
                  </td>
                  <td>
                    <div class="cell">775.1</div>
                  </td>
                  <td>
                    <div class="cell">24.9%</div>
                  </td>
                  <td>
                    <div class="cell">86479.1</div>
                  </td>
                  <td>
                    <div class="cell">4934.7</div>
                  </td>
                  <td>
                    <div class="cell">28.2%</div>
                  </td>
                  <td>
                    <div class="cell">112.8%</div>
                  </td>
                  <td>
                    <div class="cell">62965.7</div>
                  </td>
                  <td>
                    <div class="cell">2822.9</div>
                  </td>
                  <td>
                    <div class="cell">15.7%</div>
                  </td>
                  <td>
                    <div class="cell">2.6</div>
                  </td>
                  <td>
                    <div class="cell">46.9%</div>
                  </td>
                  <td>
                    <div class="cell">65.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">49</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/73a963d37fbc9af5d839d39b2075874b.png" alt="柠栀" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">柠栀</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">43</div>
                  </td>
                  <td>
                    <div class="cell">22</div>
                  </td>
                  <td>
                    <div class="cell">51.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.3</span>
                      <span class="kda2">1.5 / 1.6 / 4.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">4.4</div>
                  </td>
                  <td>
                    <div class="cell">9119.3</div>
                  </td>
                  <td>
                    <div class="cell">551.7</div>
                  </td>
                  <td>
                    <div class="cell">17.7%</div>
                  </td>
                  <td>
                    <div class="cell">44119.4</div>
                  </td>
                  <td>
                    <div class="cell">2576</div>
                  </td>
                  <td>
                    <div class="cell">14.8%</div>
                  </td>
                  <td>
                    <div class="cell">83.8%</div>
                  </td>
                  <td>
                    <div class="cell">102274.7</div>
                  </td>
                  <td>
                    <div class="cell">5145.2</div>
                  </td>
                  <td>
                    <div class="cell">28.8%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">5.4%</div>
                  </td>
                  <td>
                    <div class="cell">66.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">50</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fd5ccf7df062feca229a9d5f47fccd2d.png" alt="Ming" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Ming</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">43</div>
                  </td>
                  <td>
                    <div class="cell">22</div>
                  </td>
                  <td>
                    <div class="cell">51.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.8</span>
                      <span class="kda2">1.7 / 1.6 / 5.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">5.3</div>
                  </td>
                  <td>
                    <div class="cell">9493.8</div>
                  </td>
                  <td>
                    <div class="cell">580.2</div>
                  </td>
                  <td>
                    <div class="cell">18.6%</div>
                  </td>
                  <td>
                    <div class="cell">93480.5</div>
                  </td>
                  <td>
                    <div class="cell">5428.7</div>
                  </td>
                  <td>
                    <div class="cell">31.3%</div>
                  </td>
                  <td>
                    <div class="cell">167.7%</div>
                  </td>
                  <td>
                    <div class="cell">45783.7</div>
                  </td>
                  <td>
                    <div class="cell">2353.3</div>
                  </td>
                  <td>
                    <div class="cell">13.1%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">5.6%</div>
                  </td>
                  <td>
                    <div class="cell">73.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">51</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/beb7d3d855278db7fc92dbd7952432a8.png" alt="一曲" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">一曲</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">69</div>
                  </td>
                  <td>
                    <div class="cell">35</div>
                  </td>
                  <td>
                    <div class="cell">50.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.1</span>
                      <span class="kda2">1.3 / 1.2 / 4.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">4.9</div>
                  </td>
                  <td>
                    <div class="cell">8923.2</div>
                  </td>
                  <td>
                    <div class="cell">532</div>
                  </td>
                  <td>
                    <div class="cell">17.4%</div>
                  </td>
                  <td>
                    <div class="cell">91323.6</div>
                  </td>
                  <td>
                    <div class="cell">5106.6</div>
                  </td>
                  <td>
                    <div class="cell">29.3%</div>
                  </td>
                  <td>
                    <div class="cell">168.5%</div>
                  </td>
                  <td>
                    <div class="cell">43375.6</div>
                  </td>
                  <td>
                    <div class="cell">2171.8</div>
                  </td>
                  <td>
                    <div class="cell">11.9%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">1.3%</div>
                  </td>
                  <td>
                    <div class="cell">68.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">52</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/28b0c1c86bba11d3777e41deef12d105.png" alt="啊泽" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">啊泽</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">69</div>
                  </td>
                  <td>
                    <div class="cell">35</div>
                  </td>
                  <td>
                    <div class="cell">50.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.8</span>
                      <span class="kda2">1.4 / 2 / 4.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">4.5</div>
                  </td>
                  <td>
                    <div class="cell">9095.5</div>
                  </td>
                  <td>
                    <div class="cell">539.2</div>
                  </td>
                  <td>
                    <div class="cell">17.5%</div>
                  </td>
                  <td>
                    <div class="cell">42890</div>
                  </td>
                  <td>
                    <div class="cell">2419.1</div>
                  </td>
                  <td>
                    <div class="cell">13.7%</div>
                  </td>
                  <td>
                    <div class="cell">77.2%</div>
                  </td>
                  <td>
                    <div class="cell">103015.2</div>
                  </td>
                  <td>
                    <div class="cell">5071.2</div>
                  </td>
                  <td>
                    <div class="cell">28.1%</div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">11.8%</div>
                  </td>
                  <td>
                    <div class="cell">63.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">53</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a53645eda564019b8c18572522170a01.png" alt="小A" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小A</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">69</div>
                  </td>
                  <td>
                    <div class="cell">35</div>
                  </td>
                  <td>
                    <div class="cell">50.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.6</span>
                      <span class="kda2">0.6 / 1.4 / 6.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">6.8</div>
                  </td>
                  <td>
                    <div class="cell">7478.1</div>
                  </td>
                  <td>
                    <div class="cell">444</div>
                  </td>
                  <td>
                    <div class="cell">14.5%</div>
                  </td>
                  <td>
                    <div class="cell">33618.3</div>
                  </td>
                  <td>
                    <div class="cell">1917</div>
                  </td>
                  <td>
                    <div class="cell">10.6%</div>
                  </td>
                  <td>
                    <div class="cell">73.4%</div>
                  </td>
                  <td>
                    <div class="cell">81892.6</div>
                  </td>
                  <td>
                    <div class="cell">4158.3</div>
                  </td>
                  <td>
                    <div class="cell">22.8%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">1.8%</div>
                  </td>
                  <td>
                    <div class="cell">82.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">54</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/e97d18a7b189150074b0bf345e748842.png" alt="小玖" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小玖</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">69</div>
                  </td>
                  <td>
                    <div class="cell">35</div>
                  </td>
                  <td>
                    <div class="cell">50.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.4</span>
                      <span class="kda2">3 / 1.6 / 3.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">3.5</div>
                  </td>
                  <td>
                    <div class="cell">13365.4</div>
                  </td>
                  <td>
                    <div class="cell">791.4</div>
                  </td>
                  <td>
                    <div class="cell">25.8%</div>
                  </td>
                  <td>
                    <div class="cell">86252.4</div>
                  </td>
                  <td>
                    <div class="cell">4783.1</div>
                  </td>
                  <td>
                    <div class="cell">27.7%</div>
                  </td>
                  <td>
                    <div class="cell">107.2%</div>
                  </td>
                  <td>
                    <div class="cell">58585.3</div>
                  </td>
                  <td>
                    <div class="cell">2597.5</div>
                  </td>
                  <td>
                    <div class="cell">14.3%</div>
                  </td>
                  <td>
                    <div class="cell">2.6</div>
                  </td>
                  <td>
                    <div class="cell">43%</div>
                  </td>
                  <td>
                    <div class="cell">69.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">55</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2ee59d91feade6c3b6e42e74d289ec44.png" alt="久酷" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">久酷</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">91</div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">50.5%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.5</span>
                      <span class="kda2">0.7 / 1.2 / 6.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">6.2</div>
                  </td>
                  <td>
                    <div class="cell">6839.9</div>
                  </td>
                  <td>
                    <div class="cell">435.7</div>
                  </td>
                  <td>
                    <div class="cell">14.2%</div>
                  </td>
                  <td>
                    <div class="cell">26003.7</div>
                  </td>
                  <td>
                    <div class="cell">1587.3</div>
                  </td>
                  <td>
                    <div class="cell">9%</div>
                  </td>
                  <td>
                    <div class="cell">63.3%</div>
                  </td>
                  <td>
                    <div class="cell">74120.4</div>
                  </td>
                  <td>
                    <div class="cell">3956.4</div>
                  </td>
                  <td>
                    <div class="cell">21.8%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">1.8%</div>
                  </td>
                  <td>
                    <div class="cell">79.9%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:03</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">56</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/831ad155e862a0da8c048c80ae873aaf.png" alt="小崽" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小崽</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">50%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">6.3</span>
                      <span class="kda2">0 / 0.7 / 6.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">6.5</div>
                  </td>
                  <td>
                    <div class="cell">7121.7</div>
                  </td>
                  <td>
                    <div class="cell">457.7</div>
                  </td>
                  <td>
                    <div class="cell">15.5%</div>
                  </td>
                  <td>
                    <div class="cell">21181.7</div>
                  </td>
                  <td>
                    <div class="cell">1319</div>
                  </td>
                  <td>
                    <div class="cell">7.8%</div>
                  </td>
                  <td>
                    <div class="cell">50.2%</div>
                  </td>
                  <td>
                    <div class="cell">56979.5</div>
                  </td>
                  <td>
                    <div class="cell">3123.2</div>
                  </td>
                  <td>
                    <div class="cell">16.7%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">3.1%</div>
                  </td>
                  <td>
                    <div class="cell">93.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">57</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/3c367d6e5ca7a2b79a685f05a1eb8589.png" alt="An" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">An</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">8</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">50%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">1.2 / 2.5 / 5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">7786</div>
                  </td>
                  <td>
                    <div class="cell">460.2</div>
                  </td>
                  <td>
                    <div class="cell">15.1%</div>
                  </td>
                  <td>
                    <div class="cell">41054.7</div>
                  </td>
                  <td>
                    <div class="cell">2335.7</div>
                  </td>
                  <td>
                    <div class="cell">14%</div>
                  </td>
                  <td>
                    <div class="cell">93.2%</div>
                  </td>
                  <td>
                    <div class="cell">139448.7</div>
                  </td>
                  <td>
                    <div class="cell">6842.4</div>
                  </td>
                  <td>
                    <div class="cell">36.3%</div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">13.9%</div>
                  </td>
                  <td>
                    <div class="cell">67.1%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:38</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">58</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/12d0811490492112e295bd0409324003.png" alt="江城" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">江城</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">50%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.5</span>
                      <span class="kda2">1.7 / 1.7 / 4.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">4.7</div>
                  </td>
                  <td>
                    <div class="cell">11990.5</div>
                  </td>
                  <td>
                    <div class="cell">717</div>
                  </td>
                  <td>
                    <div class="cell">23.7%</div>
                  </td>
                  <td>
                    <div class="cell">63027</div>
                  </td>
                  <td>
                    <div class="cell">3721.8</div>
                  </td>
                  <td>
                    <div class="cell">23.7%</div>
                  </td>
                  <td>
                    <div class="cell">97.6%</div>
                  </td>
                  <td>
                    <div class="cell">53795</div>
                  </td>
                  <td>
                    <div class="cell">2666.8</div>
                  </td>
                  <td>
                    <div class="cell">14.9%</div>
                  </td>
                  <td>
                    <div class="cell">3.2</div>
                  </td>
                  <td>
                    <div class="cell">54.2%</div>
                  </td>
                  <td>
                    <div class="cell">66.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:03</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">59</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d7d43bc95a455c4acdc95c1a498e7ef2.png" alt="晨风" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">晨风</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">8</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">50%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.7</span>
                      <span class="kda2">0.8 / 1.1 / 5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">7661.8</div>
                  </td>
                  <td>
                    <div class="cell">516.7</div>
                  </td>
                  <td>
                    <div class="cell">17.1%</div>
                  </td>
                  <td>
                    <div class="cell">82041</div>
                  </td>
                  <td>
                    <div class="cell">5394.9</div>
                  </td>
                  <td>
                    <div class="cell">30.9%</div>
                  </td>
                  <td>
                    <div class="cell">179.8%</div>
                  </td>
                  <td>
                    <div class="cell">40496.3</div>
                  </td>
                  <td>
                    <div class="cell">2315.1</div>
                  </td>
                  <td>
                    <div class="cell">13.7%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">64.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">60</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0d8d108ab2c3a10240430bbecce51e2f.png" alt="一诺（徐必成）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">一诺（徐必成）</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">76</div>
                  </td>
                  <td>
                    <div class="cell">37</div>
                  </td>
                  <td>
                    <div class="cell">48.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">2.4 / 1.6 / 3.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">3.5</div>
                  </td>
                  <td>
                    <div class="cell">12704.8</div>
                  </td>
                  <td>
                    <div class="cell">794</div>
                  </td>
                  <td>
                    <div class="cell">25.6%</div>
                  </td>
                  <td>
                    <div class="cell">81580.6</div>
                  </td>
                  <td>
                    <div class="cell">4892.5</div>
                  </td>
                  <td>
                    <div class="cell">28.4%</div>
                  </td>
                  <td>
                    <div class="cell">110.8%</div>
                  </td>
                  <td>
                    <div class="cell">59199.3</div>
                  </td>
                  <td>
                    <div class="cell">2715.7</div>
                  </td>
                  <td>
                    <div class="cell">16.1%</div>
                  </td>
                  <td>
                    <div class="cell">2.7</div>
                  </td>
                  <td>
                    <div class="cell">44.2%</div>
                  </td>
                  <td>
                    <div class="cell">72.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">61</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7115f6074ac26e71cc3c750cdcd15ae0.png" alt="忆安" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">忆安</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">76</div>
                  </td>
                  <td>
                    <div class="cell">37</div>
                  </td>
                  <td>
                    <div class="cell">48.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3</span>
                      <span class="kda2">1.3 / 2 / 3.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">3.6</div>
                  </td>
                  <td>
                    <div class="cell">9023.6</div>
                  </td>
                  <td>
                    <div class="cell">561.2</div>
                  </td>
                  <td>
                    <div class="cell">18%</div>
                  </td>
                  <td>
                    <div class="cell">40360.9</div>
                  </td>
                  <td>
                    <div class="cell">2403.3</div>
                  </td>
                  <td>
                    <div class="cell">13.7%</div>
                  </td>
                  <td>
                    <div class="cell">76.3%</div>
                  </td>
                  <td>
                    <div class="cell">86828.9</div>
                  </td>
                  <td>
                    <div class="cell">4488</div>
                  </td>
                  <td>
                    <div class="cell">26.7%</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">18.8%</div>
                  </td>
                  <td>
                    <div class="cell">58.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">62</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d8f8ea8bf065993c5a039129c836e113.png" alt="长生" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">长生</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">76</div>
                  </td>
                  <td>
                    <div class="cell">37</div>
                  </td>
                  <td>
                    <div class="cell">48.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.4</span>
                      <span class="kda2">1.5 / 1.3 / 4.1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">4.1</div>
                  </td>
                  <td>
                    <div class="cell">9100.2</div>
                  </td>
                  <td>
                    <div class="cell">567.4</div>
                  </td>
                  <td>
                    <div class="cell">18.2%</div>
                  </td>
                  <td>
                    <div class="cell">95967.8</div>
                  </td>
                  <td>
                    <div class="cell">5690.4</div>
                  </td>
                  <td>
                    <div class="cell">32.7%</div>
                  </td>
                  <td>
                    <div class="cell">180.3%</div>
                  </td>
                  <td>
                    <div class="cell">44238.4</div>
                  </td>
                  <td>
                    <div class="cell">2360.2</div>
                  </td>
                  <td>
                    <div class="cell">14%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">4.1%</div>
                  </td>
                  <td>
                    <div class="cell">69.1%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">63</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/dee0b1d9815975dc77abc3f6beee2cf6.png" alt="夏竹" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">夏竹</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">76</div>
                  </td>
                  <td>
                    <div class="cell">37</div>
                  </td>
                  <td>
                    <div class="cell">48.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.4</span>
                      <span class="kda2">0.4 / 1.8 / 6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.4</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">6</div>
                  </td>
                  <td>
                    <div class="cell">7141.6</div>
                  </td>
                  <td>
                    <div class="cell">448.7</div>
                  </td>
                  <td>
                    <div class="cell">14.4%</div>
                  </td>
                  <td>
                    <div class="cell">27405.4</div>
                  </td>
                  <td>
                    <div class="cell">1619.9</div>
                  </td>
                  <td>
                    <div class="cell">9.3%</div>
                  </td>
                  <td>
                    <div class="cell">65.1%</div>
                  </td>
                  <td>
                    <div class="cell">74777.3</div>
                  </td>
                  <td>
                    <div class="cell">3996.3</div>
                  </td>
                  <td>
                    <div class="cell">23.4%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2.4%</div>
                  </td>
                  <td>
                    <div class="cell">80.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">64</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/4d3742c88bdd31560a43ff09ab5e2783.png" alt="冰然" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">冰然</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">35</div>
                  </td>
                  <td>
                    <div class="cell">17</div>
                  </td>
                  <td>
                    <div class="cell">48.5%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2.9</span>
                      <span class="kda2">1.9 / 2.5 / 3.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">3.3</div>
                  </td>
                  <td>
                    <div class="cell">12012.3</div>
                  </td>
                  <td>
                    <div class="cell">706.1</div>
                  </td>
                  <td>
                    <div class="cell">22.9%</div>
                  </td>
                  <td>
                    <div class="cell">49846.1</div>
                  </td>
                  <td>
                    <div class="cell">2739.4</div>
                  </td>
                  <td>
                    <div class="cell">16%</div>
                  </td>
                  <td>
                    <div class="cell">69.5%</div>
                  </td>
                  <td>
                    <div class="cell">90473.8</div>
                  </td>
                  <td>
                    <div class="cell">3605.7</div>
                  </td>
                  <td>
                    <div class="cell">20%</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">18.8%</div>
                  </td>
                  <td>
                    <div class="cell">60.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:47</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">65</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/eca2317db974f302eeeadb7718d4002c.png" alt="556" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">556</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">46</div>
                  </td>
                  <td>
                    <div class="cell">22</div>
                  </td>
                  <td>
                    <div class="cell">47.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.8</span>
                      <span class="kda2">0.6 / 1.9 / 6.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">6.3</div>
                  </td>
                  <td>
                    <div class="cell">7476.9</div>
                  </td>
                  <td>
                    <div class="cell">439.8</div>
                  </td>
                  <td>
                    <div class="cell">14.4%</div>
                  </td>
                  <td>
                    <div class="cell">26606.6</div>
                  </td>
                  <td>
                    <div class="cell">1422</div>
                  </td>
                  <td>
                    <div class="cell">8.2%</div>
                  </td>
                  <td>
                    <div class="cell">57.4%</div>
                  </td>
                  <td>
                    <div class="cell">87389</div>
                  </td>
                  <td>
                    <div class="cell">4331.3</div>
                  </td>
                  <td>
                    <div class="cell">23.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2%</div>
                  </td>
                  <td>
                    <div class="cell">80.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:44</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">66</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/276858cb556f317c2b5ba8735800da28.png" alt="千世" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">千世</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">47</div>
                  </td>
                  <td>
                    <div class="cell">22</div>
                  </td>
                  <td>
                    <div class="cell">46.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4</span>
                      <span class="kda2">1.2 / 2 / 4.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">4.9</div>
                  </td>
                  <td>
                    <div class="cell">9408.4</div>
                  </td>
                  <td>
                    <div class="cell">546.7</div>
                  </td>
                  <td>
                    <div class="cell">17.9%</div>
                  </td>
                  <td>
                    <div class="cell">103696.3</div>
                  </td>
                  <td>
                    <div class="cell">5553.4</div>
                  </td>
                  <td>
                    <div class="cell">31.5%</div>
                  </td>
                  <td>
                    <div class="cell">174.6%</div>
                  </td>
                  <td>
                    <div class="cell">53455.5</div>
                  </td>
                  <td>
                    <div class="cell">2607.4</div>
                  </td>
                  <td>
                    <div class="cell">14.1%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">3.6%</div>
                  </td>
                  <td>
                    <div class="cell">68.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:48</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">67</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/6476ebef7ce9703c7d6a9eef1973b92c.png" alt="佩恩" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">佩恩</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">47</div>
                  </td>
                  <td>
                    <div class="cell">22</div>
                  </td>
                  <td>
                    <div class="cell">46.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.5</span>
                      <span class="kda2">2.7 / 1.4 / 3.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.7</div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">3.4</div>
                  </td>
                  <td>
                    <div class="cell">13412.2</div>
                  </td>
                  <td>
                    <div class="cell">779.7</div>
                  </td>
                  <td>
                    <div class="cell">25.6%</div>
                  </td>
                  <td>
                    <div class="cell">90827.1</div>
                  </td>
                  <td>
                    <div class="cell">4904.9</div>
                  </td>
                  <td>
                    <div class="cell">28.2%</div>
                  </td>
                  <td>
                    <div class="cell">109.8%</div>
                  </td>
                  <td>
                    <div class="cell">63805.8</div>
                  </td>
                  <td>
                    <div class="cell">2742</div>
                  </td>
                  <td>
                    <div class="cell">14.9%</div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">45.5%</div>
                  </td>
                  <td>
                    <div class="cell">67.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:48</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">68</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/988d4be506b65f5de79bd2598d2baa2c.png" alt="爱思" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">爱思</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">15</div>
                  </td>
                  <td>
                    <div class="cell">7</div>
                  </td>
                  <td>
                    <div class="cell">46.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">6.1</span>
                      <span class="kda2">1 / 1.6 / 5.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">5.9</div>
                  </td>
                  <td>
                    <div class="cell">7075.3</div>
                  </td>
                  <td>
                    <div class="cell">455</div>
                  </td>
                  <td>
                    <div class="cell">14.4%</div>
                  </td>
                  <td>
                    <div class="cell">26492.9</div>
                  </td>
                  <td>
                    <div class="cell">1598.5</div>
                  </td>
                  <td>
                    <div class="cell">10%</div>
                  </td>
                  <td>
                    <div class="cell">69.8%</div>
                  </td>
                  <td>
                    <div class="cell">81607</div>
                  </td>
                  <td>
                    <div class="cell">4213.6</div>
                  </td>
                  <td>
                    <div class="cell">23%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0.8%</div>
                  </td>
                  <td>
                    <div class="cell">76%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:22</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">69</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a94ae4eeea3d9a98a5bf286c302e26f2.png" alt="小夜" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小夜</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">69</div>
                  </td>
                  <td>
                    <div class="cell">32</div>
                  </td>
                  <td>
                    <div class="cell">46.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.3</span>
                      <span class="kda2">2.1 / 1.9 / 3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">12134.8</div>
                  </td>
                  <td>
                    <div class="cell">735.2</div>
                  </td>
                  <td>
                    <div class="cell">24.9%</div>
                  </td>
                  <td>
                    <div class="cell">52653.9</div>
                  </td>
                  <td>
                    <div class="cell">3050.9</div>
                  </td>
                  <td>
                    <div class="cell">19.1%</div>
                  </td>
                  <td>
                    <div class="cell">77.5%</div>
                  </td>
                  <td>
                    <div class="cell">85911.6</div>
                  </td>
                  <td>
                    <div class="cell">3612.8</div>
                  </td>
                  <td>
                    <div class="cell">20.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">13.1%</div>
                  </td>
                  <td>
                    <div class="cell">63.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">70</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/b56f5210f974dc282e71b4ed4b79d16a.png" alt="梓轩" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">梓轩</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">67</div>
                  </td>
                  <td>
                    <div class="cell">31</div>
                  </td>
                  <td>
                    <div class="cell">46.2%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">1.5 / 2.1 / 3.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">3.6</div>
                  </td>
                  <td>
                    <div class="cell">8352.4</div>
                  </td>
                  <td>
                    <div class="cell">510.3</div>
                  </td>
                  <td>
                    <div class="cell">17.3%</div>
                  </td>
                  <td>
                    <div class="cell">39159.2</div>
                  </td>
                  <td>
                    <div class="cell">2318.3</div>
                  </td>
                  <td>
                    <div class="cell">14.2%</div>
                  </td>
                  <td>
                    <div class="cell">82%</div>
                  </td>
                  <td>
                    <div class="cell">88443.2</div>
                  </td>
                  <td>
                    <div class="cell">4521.3</div>
                  </td>
                  <td>
                    <div class="cell">25.4%</div>
                  </td>
                  <td>
                    <div class="cell">0.4</div>
                  </td>
                  <td>
                    <div class="cell">7.4%</div>
                  </td>
                  <td>
                    <div class="cell">62.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">71</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/04300319226899b16d9e7ade24d6e314.png" alt="以然" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">以然</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">52</div>
                  </td>
                  <td>
                    <div class="cell">24</div>
                  </td>
                  <td>
                    <div class="cell">46.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.4</span>
                      <span class="kda2">2 / 2.2 / 3.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">3.6</div>
                  </td>
                  <td>
                    <div class="cell">12145.3</div>
                  </td>
                  <td>
                    <div class="cell">699.7</div>
                  </td>
                  <td>
                    <div class="cell">23.4%</div>
                  </td>
                  <td>
                    <div class="cell">50132.4</div>
                  </td>
                  <td>
                    <div class="cell">2785</div>
                  </td>
                  <td>
                    <div class="cell">16%</div>
                  </td>
                  <td>
                    <div class="cell">69.6%</div>
                  </td>
                  <td>
                    <div class="cell">85193.8</div>
                  </td>
                  <td>
                    <div class="cell">3563</div>
                  </td>
                  <td>
                    <div class="cell">19.6%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">12.6%</div>
                  </td>
                  <td>
                    <div class="cell">60.9%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">72</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d9c3b3c3ef3da4614fb778678ce840a2.png" alt="仙语" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">仙语</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">39</div>
                  </td>
                  <td>
                    <div class="cell">18</div>
                  </td>
                  <td>
                    <div class="cell">46.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.3</span>
                      <span class="kda2">1.8 / 2.4 / 3.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">3.9</div>
                  </td>
                  <td>
                    <div class="cell">10045.6</div>
                  </td>
                  <td>
                    <div class="cell">575.8</div>
                  </td>
                  <td>
                    <div class="cell">18.9%</div>
                  </td>
                  <td>
                    <div class="cell">50901.8</div>
                  </td>
                  <td>
                    <div class="cell">2785.5</div>
                  </td>
                  <td>
                    <div class="cell">16.3%</div>
                  </td>
                  <td>
                    <div class="cell">86%</div>
                  </td>
                  <td>
                    <div class="cell">96918.6</div>
                  </td>
                  <td>
                    <div class="cell">4739.7</div>
                  </td>
                  <td>
                    <div class="cell">26.1%</div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">17.6%</div>
                  </td>
                  <td>
                    <div class="cell">64.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">73</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/cca0e32562495551f243e1f92274e547.png" alt="小久" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小久</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">61</div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">45.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5</span>
                      <span class="kda2">2.9 / 1.5 / 3.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.9</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">3.9</div>
                  </td>
                  <td>
                    <div class="cell">12914.2</div>
                  </td>
                  <td>
                    <div class="cell">778.7</div>
                  </td>
                  <td>
                    <div class="cell">25.3%</div>
                  </td>
                  <td>
                    <div class="cell">92009.8</div>
                  </td>
                  <td>
                    <div class="cell">5234.4</div>
                  </td>
                  <td>
                    <div class="cell">29.2%</div>
                  </td>
                  <td>
                    <div class="cell">115.1%</div>
                  </td>
                  <td>
                    <div class="cell">62119.2</div>
                  </td>
                  <td>
                    <div class="cell">2807.2</div>
                  </td>
                  <td>
                    <div class="cell">14.8%</div>
                  </td>
                  <td>
                    <div class="cell">3.4</div>
                  </td>
                  <td>
                    <div class="cell">56%</div>
                  </td>
                  <td>
                    <div class="cell">70.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">74</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/47767bd2507a965cf4c38eabb91b8e9a.png" alt="久凡" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">久凡</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">61</div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">45.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.8</span>
                      <span class="kda2">0.7 / 2 / 7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">7</div>
                  </td>
                  <td>
                    <div class="cell">7598.2</div>
                  </td>
                  <td>
                    <div class="cell">461.5</div>
                  </td>
                  <td>
                    <div class="cell">15%</div>
                  </td>
                  <td>
                    <div class="cell">27152.8</div>
                  </td>
                  <td>
                    <div class="cell">1561.1</div>
                  </td>
                  <td>
                    <div class="cell">8.7%</div>
                  </td>
                  <td>
                    <div class="cell">58.4%</div>
                  </td>
                  <td>
                    <div class="cell">93363.1</div>
                  </td>
                  <td>
                    <div class="cell">4784.3</div>
                  </td>
                  <td>
                    <div class="cell">25.5%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0.7%</div>
                  </td>
                  <td>
                    <div class="cell">78.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">75</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/e9a35c0f92bd12e7ca50af991b5b59a4.png" alt="迷途" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">迷途</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">61</div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">45.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2 / 2.2 / 4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">11831.8</div>
                  </td>
                  <td>
                    <div class="cell">722.2</div>
                  </td>
                  <td>
                    <div class="cell">23.4%</div>
                  </td>
                  <td>
                    <div class="cell">48689.8</div>
                  </td>
                  <td>
                    <div class="cell">2826.1</div>
                  </td>
                  <td>
                    <div class="cell">15.7%</div>
                  </td>
                  <td>
                    <div class="cell">67.6%</div>
                  </td>
                  <td>
                    <div class="cell">88897.6</div>
                  </td>
                  <td>
                    <div class="cell">3753.6</div>
                  </td>
                  <td>
                    <div class="cell">19.9%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">9.3%</div>
                  </td>
                  <td>
                    <div class="cell">60.9%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">76</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8087dfbdf220f4dbf1c2d8ced3a5faed.png" alt="阿怪" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">阿怪</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">61</div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">45.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.8</span>
                      <span class="kda2">2 / 2.6 / 4.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">2.6</div>
                  </td>
                  <td>
                    <div class="cell">4.4</div>
                  </td>
                  <td>
                    <div class="cell">9188.5</div>
                  </td>
                  <td>
                    <div class="cell">555.4</div>
                  </td>
                  <td>
                    <div class="cell">18.1%</div>
                  </td>
                  <td>
                    <div class="cell">47240.8</div>
                  </td>
                  <td>
                    <div class="cell">2764.9</div>
                  </td>
                  <td>
                    <div class="cell">15.3%</div>
                  </td>
                  <td>
                    <div class="cell">85.4%</div>
                  </td>
                  <td>
                    <div class="cell">101014.9</div>
                  </td>
                  <td>
                    <div class="cell">4993.6</div>
                  </td>
                  <td>
                    <div class="cell">27%</div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">13.9%</div>
                  </td>
                  <td>
                    <div class="cell">68.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">77</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/98b7d418ea608c3f940042b2c9318285.png" alt="笑影" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">笑影</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">61</div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">45.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">1.3 / 1.8 / 4.1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">4.1</div>
                  </td>
                  <td>
                    <div class="cell">8820.6</div>
                  </td>
                  <td>
                    <div class="cell">530.9</div>
                  </td>
                  <td>
                    <div class="cell">18.1%</div>
                  </td>
                  <td>
                    <div class="cell">83904</div>
                  </td>
                  <td>
                    <div class="cell">4822.4</div>
                  </td>
                  <td>
                    <div class="cell">29.7%</div>
                  </td>
                  <td>
                    <div class="cell">164.1%</div>
                  </td>
                  <td>
                    <div class="cell">49334.2</div>
                  </td>
                  <td>
                    <div class="cell">2620.3</div>
                  </td>
                  <td>
                    <div class="cell">14.6%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">3%</div>
                  </td>
                  <td>
                    <div class="cell">68.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">78</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/48a2ded453710c49b80989954dea1922.png" alt="情缘" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">情缘</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">61</div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">45.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5</span>
                      <span class="kda2">1.7 / 1.5 / 5.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">5.2</div>
                  </td>
                  <td>
                    <div class="cell">9166</div>
                  </td>
                  <td>
                    <div class="cell">553.2</div>
                  </td>
                  <td>
                    <div class="cell">18%</div>
                  </td>
                  <td>
                    <div class="cell">100121.9</div>
                  </td>
                  <td>
                    <div class="cell">5600.3</div>
                  </td>
                  <td>
                    <div class="cell">30.8%</div>
                  </td>
                  <td>
                    <div class="cell">171.5%</div>
                  </td>
                  <td>
                    <div class="cell">45333.7</div>
                  </td>
                  <td>
                    <div class="cell">2390.4</div>
                  </td>
                  <td>
                    <div class="cell">12.7%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2.2%</div>
                  </td>
                  <td>
                    <div class="cell">72%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">79</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fbe28816578b5b5dcb758ce547ac5818.png" alt="晚星" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">晚星</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">24</div>
                  </td>
                  <td>
                    <div class="cell">11</div>
                  </td>
                  <td>
                    <div class="cell">45.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">2.2 / 2 / 3.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">3.7</div>
                  </td>
                  <td>
                    <div class="cell">12445.7</div>
                  </td>
                  <td>
                    <div class="cell">705.6</div>
                  </td>
                  <td>
                    <div class="cell">23.3%</div>
                  </td>
                  <td>
                    <div class="cell">57792.8</div>
                  </td>
                  <td>
                    <div class="cell">3160.3</div>
                  </td>
                  <td>
                    <div class="cell">17.4%</div>
                  </td>
                  <td>
                    <div class="cell">75.8%</div>
                  </td>
                  <td>
                    <div class="cell">109936.7</div>
                  </td>
                  <td>
                    <div class="cell">4586.8</div>
                  </td>
                  <td>
                    <div class="cell">25%</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">18.7%</div>
                  </td>
                  <td>
                    <div class="cell">70.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:18:08</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">80</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/98e4fa9e72db8735209227f4f121b562.png" alt="东方" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">东方</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">57</div>
                  </td>
                  <td>
                    <div class="cell">26</div>
                  </td>
                  <td>
                    <div class="cell">45.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.4</span>
                      <span class="kda2">1.9 / 2 / 3.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">3.4</div>
                  </td>
                  <td>
                    <div class="cell">8752.3</div>
                  </td>
                  <td>
                    <div class="cell">566</div>
                  </td>
                  <td>
                    <div class="cell">18.5%</div>
                  </td>
                  <td>
                    <div class="cell">45276.5</div>
                  </td>
                  <td>
                    <div class="cell">2778.2</div>
                  </td>
                  <td>
                    <div class="cell">15.5%</div>
                  </td>
                  <td>
                    <div class="cell">82.5%</div>
                  </td>
                  <td>
                    <div class="cell">87612</div>
                  </td>
                  <td>
                    <div class="cell">4588</div>
                  </td>
                  <td>
                    <div class="cell">25.4%</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">17.4%</div>
                  </td>
                  <td>
                    <div class="cell">63.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:46</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">81</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7c19f73653eebeb163b7861ce9961e6a.png" alt="花云" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">花云</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">68</div>
                  </td>
                  <td>
                    <div class="cell">31</div>
                  </td>
                  <td>
                    <div class="cell">45.5%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">2.5 / 1.5 / 2.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">2.9</div>
                  </td>
                  <td>
                    <div class="cell">12185.8</div>
                  </td>
                  <td>
                    <div class="cell">734.6</div>
                  </td>
                  <td>
                    <div class="cell">25%</div>
                  </td>
                  <td>
                    <div class="cell">82239.7</div>
                  </td>
                  <td>
                    <div class="cell">4596.7</div>
                  </td>
                  <td>
                    <div class="cell">28.1%</div>
                  </td>
                  <td>
                    <div class="cell">112%</div>
                  </td>
                  <td>
                    <div class="cell">56037.6</div>
                  </td>
                  <td>
                    <div class="cell">2579.9</div>
                  </td>
                  <td>
                    <div class="cell">14.5%</div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">45.4%</div>
                  </td>
                  <td>
                    <div class="cell">70%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">82</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/f019291412bf15426a5cbc39afd18591.png" alt="冰尘" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">冰尘</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">66</div>
                  </td>
                  <td>
                    <div class="cell">30</div>
                  </td>
                  <td>
                    <div class="cell">45.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">5.5</span>
                      <span class="kda2">0.5 / 1.3 / 6.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">6.3</div>
                  </td>
                  <td>
                    <div class="cell">7302.2</div>
                  </td>
                  <td>
                    <div class="cell">428.3</div>
                  </td>
                  <td>
                    <div class="cell">14.3%</div>
                  </td>
                  <td>
                    <div class="cell">25182</div>
                  </td>
                  <td>
                    <div class="cell">1408.9</div>
                  </td>
                  <td>
                    <div class="cell">8.4%</div>
                  </td>
                  <td>
                    <div class="cell">58.6%</div>
                  </td>
                  <td>
                    <div class="cell">90739</div>
                  </td>
                  <td>
                    <div class="cell">4575</div>
                  </td>
                  <td>
                    <div class="cell">24.4%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">1.2%</div>
                  </td>
                  <td>
                    <div class="cell">78.1%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">83</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9b3cef40ec005b398e2e6c78d733eb70.png" alt="苏沫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">苏沫</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">66</div>
                  </td>
                  <td>
                    <div class="cell">30</div>
                  </td>
                  <td>
                    <div class="cell">45.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.8</span>
                      <span class="kda2">1.6 / 2 / 4.1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">4.1</div>
                  </td>
                  <td>
                    <div class="cell">9244.4</div>
                  </td>
                  <td>
                    <div class="cell">544.8</div>
                  </td>
                  <td>
                    <div class="cell">18.2%</div>
                  </td>
                  <td>
                    <div class="cell">37527</div>
                  </td>
                  <td>
                    <div class="cell">2141</div>
                  </td>
                  <td>
                    <div class="cell">12.6%</div>
                  </td>
                  <td>
                    <div class="cell">68.2%</div>
                  </td>
                  <td>
                    <div class="cell">102027.7</div>
                  </td>
                  <td>
                    <div class="cell">4994</div>
                  </td>
                  <td>
                    <div class="cell">27%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">8.8%</div>
                  </td>
                  <td>
                    <div class="cell">64.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">84</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/47e30493ec817b2c34cf5c82f5b58d9c.png" alt="幕色" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">幕色</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">66</div>
                  </td>
                  <td>
                    <div class="cell">30</div>
                  </td>
                  <td>
                    <div class="cell">45.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.6</span>
                      <span class="kda2">1.3 / 1.5 / 4.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">4.6</div>
                  </td>
                  <td>
                    <div class="cell">8954.9</div>
                  </td>
                  <td>
                    <div class="cell">523.4</div>
                  </td>
                  <td>
                    <div class="cell">17.5%</div>
                  </td>
                  <td>
                    <div class="cell">101989.7</div>
                  </td>
                  <td>
                    <div class="cell">5631.9</div>
                  </td>
                  <td>
                    <div class="cell">33%</div>
                  </td>
                  <td>
                    <div class="cell">189.2%</div>
                  </td>
                  <td>
                    <div class="cell">45423.4</div>
                  </td>
                  <td>
                    <div class="cell">2326.4</div>
                  </td>
                  <td>
                    <div class="cell">12.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">1.5%</div>
                  </td>
                  <td>
                    <div class="cell">65.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">85</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fcdd4da0c20422cebc71a35df5a20bfb.png" alt="蓝桉" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">蓝桉</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">66</div>
                  </td>
                  <td>
                    <div class="cell">30</div>
                  </td>
                  <td>
                    <div class="cell">45.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">2.5 / 1.5 / 3.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">3.6</div>
                  </td>
                  <td>
                    <div class="cell">13367.4</div>
                  </td>
                  <td>
                    <div class="cell">778.8</div>
                  </td>
                  <td>
                    <div class="cell">26.1%</div>
                  </td>
                  <td>
                    <div class="cell">93654.3</div>
                  </td>
                  <td>
                    <div class="cell">5127.9</div>
                  </td>
                  <td>
                    <div class="cell">29.7%</div>
                  </td>
                  <td>
                    <div class="cell">113.2%</div>
                  </td>
                  <td>
                    <div class="cell">67230.5</div>
                  </td>
                  <td>
                    <div class="cell">3028.9</div>
                  </td>
                  <td>
                    <div class="cell">16.5%</div>
                  </td>
                  <td>
                    <div class="cell">2.7</div>
                  </td>
                  <td>
                    <div class="cell">47.5%</div>
                  </td>
                  <td>
                    <div class="cell">66.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">86</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/b01cb2ce26a07a06bc519a6ff847b59a.png" alt="星痕" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">星痕</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">62</div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">45.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.3</span>
                      <span class="kda2">1.4 / 2 / 3.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">3.7</div>
                  </td>
                  <td>
                    <div class="cell">8381.7</div>
                  </td>
                  <td>
                    <div class="cell">549.6</div>
                  </td>
                  <td>
                    <div class="cell">18.1%</div>
                  </td>
                  <td>
                    <div class="cell">76101.1</div>
                  </td>
                  <td>
                    <div class="cell">4600.8</div>
                  </td>
                  <td>
                    <div class="cell">25.7%</div>
                  </td>
                  <td>
                    <div class="cell">139.9%</div>
                  </td>
                  <td>
                    <div class="cell">49449.5</div>
                  </td>
                  <td>
                    <div class="cell">2787.1</div>
                  </td>
                  <td>
                    <div class="cell">15.6%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">1.9%</div>
                  </td>
                  <td>
                    <div class="cell">65.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:36</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">87</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/92b982171748e8d0e08e29d817e4d164.png" alt="不弃" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">不弃</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">67</div>
                  </td>
                  <td>
                    <div class="cell">30</div>
                  </td>
                  <td>
                    <div class="cell">44.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">0.3 / 1.5 / 5.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">5.9</div>
                  </td>
                  <td>
                    <div class="cell">7186.5</div>
                  </td>
                  <td>
                    <div class="cell">435</div>
                  </td>
                  <td>
                    <div class="cell">14.8%</div>
                  </td>
                  <td>
                    <div class="cell">25157.3</div>
                  </td>
                  <td>
                    <div class="cell">1437.1</div>
                  </td>
                  <td>
                    <div class="cell">8.8%</div>
                  </td>
                  <td>
                    <div class="cell">59.7%</div>
                  </td>
                  <td>
                    <div class="cell">83956.5</div>
                  </td>
                  <td>
                    <div class="cell">4356.8</div>
                  </td>
                  <td>
                    <div class="cell">24.8%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">4.1%</div>
                  </td>
                  <td>
                    <div class="cell">77.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:54</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">88</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8ae1b3437b077613bd309aa15bbee728.png" alt="酷偕" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">酷偕</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">32</div>
                  </td>
                  <td>
                    <div class="cell">14</div>
                  </td>
                  <td>
                    <div class="cell">43.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.5</span>
                      <span class="kda2">1.3 / 1.9 / 3.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">3.7</div>
                  </td>
                  <td>
                    <div class="cell">8675.7</div>
                  </td>
                  <td>
                    <div class="cell">547.9</div>
                  </td>
                  <td>
                    <div class="cell">17.9%</div>
                  </td>
                  <td>
                    <div class="cell">43129.3</div>
                  </td>
                  <td>
                    <div class="cell">2621</div>
                  </td>
                  <td>
                    <div class="cell">15.4%</div>
                  </td>
                  <td>
                    <div class="cell">86.6%</div>
                  </td>
                  <td>
                    <div class="cell">93694.3</div>
                  </td>
                  <td>
                    <div class="cell">4947.3</div>
                  </td>
                  <td>
                    <div class="cell">29.2%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">14.7%</div>
                  </td>
                  <td>
                    <div class="cell">62.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:13</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">89</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/1e8f31a72ea4d38212bdbf473c55ee9e.png" alt="梓凡" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">梓凡</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">7</div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">42.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">3.2 / 2.8 / 3.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3.2</div>
                  </td>
                  <td>
                    <div class="cell">2.8</div>
                  </td>
                  <td>
                    <div class="cell">3.4</div>
                  </td>
                  <td>
                    <div class="cell">14170.2</div>
                  </td>
                  <td>
                    <div class="cell">762.7</div>
                  </td>
                  <td>
                    <div class="cell">26.1%</div>
                  </td>
                  <td>
                    <div class="cell">53272.1</div>
                  </td>
                  <td>
                    <div class="cell">2773.8</div>
                  </td>
                  <td>
                    <div class="cell">16.6%</div>
                  </td>
                  <td>
                    <div class="cell">63.6%</div>
                  </td>
                  <td>
                    <div class="cell">84873.7</div>
                  </td>
                  <td>
                    <div class="cell">3307.8</div>
                  </td>
                  <td>
                    <div class="cell">17.4%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">5.8%</div>
                  </td>
                  <td>
                    <div class="cell">69.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:18:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">90</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/926ae6a4e63c48e1ec989ae0df604f0f.png" alt="顾兴" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">顾兴</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">14</div>
                  </td>
                  <td>
                    <div class="cell">6</div>
                  </td>
                  <td>
                    <div class="cell">42.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.5</span>
                      <span class="kda2">2 / 1.3 / 2.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">2.3</div>
                  </td>
                  <td>
                    <div class="cell">11787.7</div>
                  </td>
                  <td>
                    <div class="cell">739.1</div>
                  </td>
                  <td>
                    <div class="cell">24.6%</div>
                  </td>
                  <td>
                    <div class="cell">45685.3</div>
                  </td>
                  <td>
                    <div class="cell">2840.5</div>
                  </td>
                  <td>
                    <div class="cell">16.6%</div>
                  </td>
                  <td>
                    <div class="cell">70.3%</div>
                  </td>
                  <td>
                    <div class="cell">82417.7</div>
                  </td>
                  <td>
                    <div class="cell">3635.5</div>
                  </td>
                  <td>
                    <div class="cell">18.6%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">9.4%</div>
                  </td>
                  <td>
                    <div class="cell">58.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:28</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">91</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5def77d9d240b0e5fd44cdf3ed78f41d.png" alt="情川" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">情川</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">31</div>
                  </td>
                  <td>
                    <div class="cell">13</div>
                  </td>
                  <td>
                    <div class="cell">41.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.5</span>
                      <span class="kda2">1 / 1.6 / 3.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">3.8</div>
                  </td>
                  <td>
                    <div class="cell">8286.3</div>
                  </td>
                  <td>
                    <div class="cell">540.2</div>
                  </td>
                  <td>
                    <div class="cell">17.9%</div>
                  </td>
                  <td>
                    <div class="cell">35620.1</div>
                  </td>
                  <td>
                    <div class="cell">2286.4</div>
                  </td>
                  <td>
                    <div class="cell">13.7%</div>
                  </td>
                  <td>
                    <div class="cell">74.8%</div>
                  </td>
                  <td>
                    <div class="cell">93415.3</div>
                  </td>
                  <td>
                    <div class="cell">4851.1</div>
                  </td>
                  <td>
                    <div class="cell">28.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">13.9%</div>
                  </td>
                  <td>
                    <div class="cell">70.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:13</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">92</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/84ebf5c426b75033b4e1df73fbe5cf2a.png" alt="决明" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">决明</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">22</div>
                  </td>
                  <td>
                    <div class="cell">9</div>
                  </td>
                  <td>
                    <div class="cell">40.9%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">1 / 1.3 / 3.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">3.5</div>
                  </td>
                  <td>
                    <div class="cell">8862.1</div>
                  </td>
                  <td>
                    <div class="cell">536.2</div>
                  </td>
                  <td>
                    <div class="cell">17.6%</div>
                  </td>
                  <td>
                    <div class="cell">99848.8</div>
                  </td>
                  <td>
                    <div class="cell">5459.9</div>
                  </td>
                  <td>
                    <div class="cell">31.1%</div>
                  </td>
                  <td>
                    <div class="cell">177.2%</div>
                  </td>
                  <td>
                    <div class="cell">42921.9</div>
                  </td>
                  <td>
                    <div class="cell">2230.5</div>
                  </td>
                  <td>
                    <div class="cell">13.2%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">4.6%</div>
                  </td>
                  <td>
                    <div class="cell">57.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">93</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7bcd79d0e0a980c3b116ed2b2a27b0d7.png" alt="林一" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">林一</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">40%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2.7</span>
                      <span class="kda2">1.8 / 1.8 / 2.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">12833.4</div>
                  </td>
                  <td>
                    <div class="cell">808.6</div>
                  </td>
                  <td>
                    <div class="cell">26.3%</div>
                  </td>
                  <td>
                    <div class="cell">41055</div>
                  </td>
                  <td>
                    <div class="cell">2481.8</div>
                  </td>
                  <td>
                    <div class="cell">14.6%</div>
                  </td>
                  <td>
                    <div class="cell">55.4%</div>
                  </td>
                  <td>
                    <div class="cell">76414.8</div>
                  </td>
                  <td>
                    <div class="cell">3165.6</div>
                  </td>
                  <td>
                    <div class="cell">18.5%</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">31.3%</div>
                  </td>
                  <td>
                    <div class="cell">57.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:23</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">94</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/cdd628c5a4e9fffa672d0df64fb110da.png" alt="灵梦" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">灵梦</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">40</div>
                  </td>
                  <td>
                    <div class="cell">16</div>
                  </td>
                  <td>
                    <div class="cell">40%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">1.3 / 1.5 / 4.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">4.8</div>
                  </td>
                  <td>
                    <div class="cell">9069.8</div>
                  </td>
                  <td>
                    <div class="cell">565.7</div>
                  </td>
                  <td>
                    <div class="cell">18.7%</div>
                  </td>
                  <td>
                    <div class="cell">88761</div>
                  </td>
                  <td>
                    <div class="cell">5120.1</div>
                  </td>
                  <td>
                    <div class="cell">29.7%</div>
                  </td>
                  <td>
                    <div class="cell">158.5%</div>
                  </td>
                  <td>
                    <div class="cell">45148.4</div>
                  </td>
                  <td>
                    <div class="cell">2363</div>
                  </td>
                  <td>
                    <div class="cell">13.8%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">5.8%</div>
                  </td>
                  <td>
                    <div class="cell">71.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:38</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">95</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9f4f7b1b8aefb81a33a98c843d4fc3cc.png" alt="九月" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">九月</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">40</div>
                  </td>
                  <td>
                    <div class="cell">16</div>
                  </td>
                  <td>
                    <div class="cell">40%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.2</span>
                      <span class="kda2">3 / 1.7 / 2.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">2.9</div>
                  </td>
                  <td>
                    <div class="cell">11360.8</div>
                  </td>
                  <td>
                    <div class="cell">712.7</div>
                  </td>
                  <td>
                    <div class="cell">23.5%</div>
                  </td>
                  <td>
                    <div class="cell">45366.9</div>
                  </td>
                  <td>
                    <div class="cell">2685.2</div>
                  </td>
                  <td>
                    <div class="cell">15.7%</div>
                  </td>
                  <td>
                    <div class="cell">68.3%</div>
                  </td>
                  <td>
                    <div class="cell">77803.4</div>
                  </td>
                  <td>
                    <div class="cell">3146.2</div>
                  </td>
                  <td>
                    <div class="cell">18.3%</div>
                  </td>
                  <td>
                    <div class="cell">0.9</div>
                  </td>
                  <td>
                    <div class="cell">14.8%</div>
                  </td>
                  <td>
                    <div class="cell">64.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:38</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">96</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/43b28d3e73ace965ee0bd5561258bace.png" alt="秀豆" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">秀豆</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">40</div>
                  </td>
                  <td>
                    <div class="cell">16</div>
                  </td>
                  <td>
                    <div class="cell">40%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4</span>
                      <span class="kda2">2.3 / 1.4 / 3.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.3</div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">3.4</div>
                  </td>
                  <td>
                    <div class="cell">12141.6</div>
                  </td>
                  <td>
                    <div class="cell">756.6</div>
                  </td>
                  <td>
                    <div class="cell">25%</div>
                  </td>
                  <td>
                    <div class="cell">89104.4</div>
                  </td>
                  <td>
                    <div class="cell">5230.3</div>
                  </td>
                  <td>
                    <div class="cell">30.5%</div>
                  </td>
                  <td>
                    <div class="cell">121.4%</div>
                  </td>
                  <td>
                    <div class="cell">55297.8</div>
                  </td>
                  <td>
                    <div class="cell">2594</div>
                  </td>
                  <td>
                    <div class="cell">15.4%</div>
                  </td>
                  <td>
                    <div class="cell">2.7</div>
                  </td>
                  <td>
                    <div class="cell">47.1%</div>
                  </td>
                  <td>
                    <div class="cell">62.1%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:38</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">97</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a21c30d04be583356cb6e8cffb89529e.png" alt="稚念" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">稚念</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">38</div>
                  </td>
                  <td>
                    <div class="cell">15</div>
                  </td>
                  <td>
                    <div class="cell">39.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.8</span>
                      <span class="kda2">0.4 / 1.3 / 5.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.4</div>
                  </td>
                  <td>
                    <div class="cell">1.3</div>
                  </td>
                  <td>
                    <div class="cell">5.2</div>
                  </td>
                  <td>
                    <div class="cell">7109.4</div>
                  </td>
                  <td>
                    <div class="cell">431</div>
                  </td>
                  <td>
                    <div class="cell">14.3%</div>
                  </td>
                  <td>
                    <div class="cell">28453.3</div>
                  </td>
                  <td>
                    <div class="cell">1525.7</div>
                  </td>
                  <td>
                    <div class="cell">8.4%</div>
                  </td>
                  <td>
                    <div class="cell">59.5%</div>
                  </td>
                  <td>
                    <div class="cell">71258.4</div>
                  </td>
                  <td>
                    <div class="cell">3641.6</div>
                  </td>
                  <td>
                    <div class="cell">21.6%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2.4%</div>
                  </td>
                  <td>
                    <div class="cell">78.8%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">98</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0cdf1dd856cab1fd5475977c82f9d658.png" alt="钎城" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">钎城</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">38</div>
                  </td>
                  <td>
                    <div class="cell">15</div>
                  </td>
                  <td>
                    <div class="cell">39.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">1.7 / 1.1 / 2.9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">2.9</div>
                  </td>
                  <td>
                    <div class="cell">12387.1</div>
                  </td>
                  <td>
                    <div class="cell">734.8</div>
                  </td>
                  <td>
                    <div class="cell">24.5%</div>
                  </td>
                  <td>
                    <div class="cell">88089.7</div>
                  </td>
                  <td>
                    <div class="cell">4777</div>
                  </td>
                  <td>
                    <div class="cell">27.5%</div>
                  </td>
                  <td>
                    <div class="cell">110.8%</div>
                  </td>
                  <td>
                    <div class="cell">59939.7</div>
                  </td>
                  <td>
                    <div class="cell">2617.5</div>
                  </td>
                  <td>
                    <div class="cell">16%</div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">45.7%</div>
                  </td>
                  <td>
                    <div class="cell">66.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">99</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7711821e098a9853ce69bd6903b907cc.png" alt="小义" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小义</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">38</div>
                  </td>
                  <td>
                    <div class="cell">15</div>
                  </td>
                  <td>
                    <div class="cell">39.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2.7 / 1.9 / 2.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.7</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">12769.9</div>
                  </td>
                  <td>
                    <div class="cell">764.2</div>
                  </td>
                  <td>
                    <div class="cell">25.4%</div>
                  </td>
                  <td>
                    <div class="cell">55972.6</div>
                  </td>
                  <td>
                    <div class="cell">3209</div>
                  </td>
                  <td>
                    <div class="cell">18.6%</div>
                  </td>
                  <td>
                    <div class="cell">74.6%</div>
                  </td>
                  <td>
                    <div class="cell">83710.8</div>
                  </td>
                  <td>
                    <div class="cell">3347.3</div>
                  </td>
                  <td>
                    <div class="cell">19.9%</div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">10.8%</div>
                  </td>
                  <td>
                    <div class="cell">74.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">100</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/268ab209ef89f2aa4bd81b452e9bac26.png" alt="文帝" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">文帝</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">16</div>
                  </td>
                  <td>
                    <div class="cell">6</div>
                  </td>
                  <td>
                    <div class="cell">37.5%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.2</span>
                      <span class="kda2">1.1 / 1.1 / 3.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">1.1</div>
                  </td>
                  <td>
                    <div class="cell">3.7</div>
                  </td>
                  <td>
                    <div class="cell">9161.8</div>
                  </td>
                  <td>
                    <div class="cell">529.7</div>
                  </td>
                  <td>
                    <div class="cell">18%</div>
                  </td>
                  <td>
                    <div class="cell">113626</div>
                  </td>
                  <td>
                    <div class="cell">5887.6</div>
                  </td>
                  <td>
                    <div class="cell">33.6%</div>
                  </td>
                  <td>
                    <div class="cell">187%</div>
                  </td>
                  <td>
                    <div class="cell">42583.8</div>
                  </td>
                  <td>
                    <div class="cell">2155.7</div>
                  </td>
                  <td>
                    <div class="cell">12%</div>
                  </td>
                  <td>
                    <div class="cell">0.4</div>
                  </td>
                  <td>
                    <div class="cell">4.7%</div>
                  </td>
                  <td>
                    <div class="cell">72%</div>
                  </td>
                  <td>
                    <div class="cell">00:17:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">101</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0af445ace86a94640448d1b6cd810d05.png" alt="小椿" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小椿</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">23</div>
                  </td>
                  <td>
                    <div class="cell">8</div>
                  </td>
                  <td>
                    <div class="cell">34.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2.7</span>
                      <span class="kda2">1.9 / 2.2 / 2.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">11862</div>
                  </td>
                  <td>
                    <div class="cell">750.2</div>
                  </td>
                  <td>
                    <div class="cell">24.4%</div>
                  </td>
                  <td>
                    <div class="cell">42474.4</div>
                  </td>
                  <td>
                    <div class="cell">2650.5</div>
                  </td>
                  <td>
                    <div class="cell">15.3%</div>
                  </td>
                  <td>
                    <div class="cell">62.6%</div>
                  </td>
                  <td>
                    <div class="cell">68462</div>
                  </td>
                  <td>
                    <div class="cell">3080.3</div>
                  </td>
                  <td>
                    <div class="cell">18.1%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">8.5%</div>
                  </td>
                  <td>
                    <div class="cell">61.4%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:32</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">102</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ab0ad160d0a21ab9186176d1b819da39.png" alt="季节" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">季节</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">33.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2.5</span>
                      <span class="kda2">2 / 2.6 / 4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">2.6</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">10830.3</div>
                  </td>
                  <td>
                    <div class="cell">812.3</div>
                  </td>
                  <td>
                    <div class="cell">26.8%</div>
                  </td>
                  <td>
                    <div class="cell">53605.3</div>
                  </td>
                  <td>
                    <div class="cell">3779</div>
                  </td>
                  <td>
                    <div class="cell">18.5%</div>
                  </td>
                  <td>
                    <div class="cell">70.5%</div>
                  </td>
                  <td>
                    <div class="cell">81531</div>
                  </td>
                  <td>
                    <div class="cell">4440.8</div>
                  </td>
                  <td>
                    <div class="cell">20.6%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">53.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:13:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">103</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d0f5e9f6fee630bf5519cae6d1da095a.png" alt="无上" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">无上</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">33.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2</span>
                      <span class="kda2">0 / 1.6 / 3.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">3.3</div>
                  </td>
                  <td>
                    <div class="cell">5697</div>
                  </td>
                  <td>
                    <div class="cell">460</div>
                  </td>
                  <td>
                    <div class="cell">15.3%</div>
                  </td>
                  <td>
                    <div class="cell">23217</div>
                  </td>
                  <td>
                    <div class="cell">1751.4</div>
                  </td>
                  <td>
                    <div class="cell">11.1%</div>
                  </td>
                  <td>
                    <div class="cell">72.4%</div>
                  </td>
                  <td>
                    <div class="cell">89203</div>
                  </td>
                  <td>
                    <div class="cell">6178.2</div>
                  </td>
                  <td>
                    <div class="cell">32.4%</div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">6.6%</div>
                  </td>
                  <td>
                    <div class="cell">47.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:13:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">104</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/573ca193e4c832d81953b2245713471e.png" alt="小磊" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小磊</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">28</div>
                  </td>
                  <td>
                    <div class="cell">9</div>
                  </td>
                  <td>
                    <div class="cell">32.1%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4</span>
                      <span class="kda2">0.7 / 2 / 5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">6608.7</div>
                  </td>
                  <td>
                    <div class="cell">426.2</div>
                  </td>
                  <td>
                    <div class="cell">14.4%</div>
                  </td>
                  <td>
                    <div class="cell">24547.2</div>
                  </td>
                  <td>
                    <div class="cell">1518.9</div>
                  </td>
                  <td>
                    <div class="cell">9.6%</div>
                  </td>
                  <td>
                    <div class="cell">66.5%</div>
                  </td>
                  <td>
                    <div class="cell">75094.6</div>
                  </td>
                  <td>
                    <div class="cell">4007.4</div>
                  </td>
                  <td>
                    <div class="cell">20.4%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0.9%</div>
                  </td>
                  <td>
                    <div class="cell">67%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">105</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2ddaf7b8d271e9ed87a458ec48c946bc.png" alt="小年" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小年</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">37</div>
                  </td>
                  <td>
                    <div class="cell">11</div>
                  </td>
                  <td>
                    <div class="cell">29.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.2</span>
                      <span class="kda2">2 / 2.1 / 3.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">3.3</div>
                  </td>
                  <td>
                    <div class="cell">11611.5</div>
                  </td>
                  <td>
                    <div class="cell">737.7</div>
                  </td>
                  <td>
                    <div class="cell">24.9%</div>
                  </td>
                  <td>
                    <div class="cell">85532.3</div>
                  </td>
                  <td>
                    <div class="cell">5076.7</div>
                  </td>
                  <td>
                    <div class="cell">29.6%</div>
                  </td>
                  <td>
                    <div class="cell">118.6%</div>
                  </td>
                  <td>
                    <div class="cell">65648.7</div>
                  </td>
                  <td>
                    <div class="cell">3271.7</div>
                  </td>
                  <td>
                    <div class="cell">17.4%</div>
                  </td>
                  <td>
                    <div class="cell">1.9</div>
                  </td>
                  <td>
                    <div class="cell">37.1%</div>
                  </td>
                  <td>
                    <div class="cell">67.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:10</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">106</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/f9506254c198d2d0db3fff0527893892.png" alt="末将" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">末将</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">37</div>
                  </td>
                  <td>
                    <div class="cell">11</div>
                  </td>
                  <td>
                    <div class="cell">29.7%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.7</span>
                      <span class="kda2">1.6 / 1.6 / 3.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">1.6</div>
                  </td>
                  <td>
                    <div class="cell">3.7</div>
                  </td>
                  <td>
                    <div class="cell">8605.8</div>
                  </td>
                  <td>
                    <div class="cell">547.2</div>
                  </td>
                  <td>
                    <div class="cell">18.5%</div>
                  </td>
                  <td>
                    <div class="cell">89828.8</div>
                  </td>
                  <td>
                    <div class="cell">5165.9</div>
                  </td>
                  <td>
                    <div class="cell">29.6%</div>
                  </td>
                  <td>
                    <div class="cell">159.4%</div>
                  </td>
                  <td>
                    <div class="cell">42484.2</div>
                  </td>
                  <td>
                    <div class="cell">2472.5</div>
                  </td>
                  <td>
                    <div class="cell">12.9%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">3.5%</div>
                  </td>
                  <td>
                    <div class="cell">66.1%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:10</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">107</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8ee4721ed5162f123e89bcc47a30d0e3.png" alt="Qy" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Qy</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">34</div>
                  </td>
                  <td>
                    <div class="cell">10</div>
                  </td>
                  <td>
                    <div class="cell">29.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.3</span>
                      <span class="kda2">2.2 / 2 / 2.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">2.8</div>
                  </td>
                  <td>
                    <div class="cell">11472.8</div>
                  </td>
                  <td>
                    <div class="cell">717.6</div>
                  </td>
                  <td>
                    <div class="cell">24.2%</div>
                  </td>
                  <td>
                    <div class="cell">49381.1</div>
                  </td>
                  <td>
                    <div class="cell">2865.5</div>
                  </td>
                  <td>
                    <div class="cell">16.9%</div>
                  </td>
                  <td>
                    <div class="cell">70.5%</div>
                  </td>
                  <td>
                    <div class="cell">89982.4</div>
                  </td>
                  <td>
                    <div class="cell">4057.3</div>
                  </td>
                  <td>
                    <div class="cell">21.4%</div>
                  </td>
                  <td>
                    <div class="cell">0.8</div>
                  </td>
                  <td>
                    <div class="cell">21.4%</div>
                  </td>
                  <td>
                    <div class="cell">65.9%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:22</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">108</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/4d6d01c683acf5694978910995f9a3eb.png" alt="背影" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">背影</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">34</div>
                  </td>
                  <td>
                    <div class="cell">10</div>
                  </td>
                  <td>
                    <div class="cell">29.4%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.4</span>
                      <span class="kda2">1 / 2.2 / 4.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">4.5</div>
                  </td>
                  <td>
                    <div class="cell">8263.5</div>
                  </td>
                  <td>
                    <div class="cell">515.1</div>
                  </td>
                  <td>
                    <div class="cell">17.4%</div>
                  </td>
                  <td>
                    <div class="cell">39122.8</div>
                  </td>
                  <td>
                    <div class="cell">2321.4</div>
                  </td>
                  <td>
                    <div class="cell">13.9%</div>
                  </td>
                  <td>
                    <div class="cell">80.5%</div>
                  </td>
                  <td>
                    <div class="cell">95159</div>
                  </td>
                  <td>
                    <div class="cell">5139.6</div>
                  </td>
                  <td>
                    <div class="cell">27%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">9.6%</div>
                  </td>
                  <td>
                    <div class="cell">64.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:26</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">109</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/35faba2f440631c6314f9aae67c25f83.png" alt="杰杰" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">杰杰</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">7</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">28.5%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.1</span>
                      <span class="kda2">0.7 / 2.5 / 4.4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">2.5</div>
                  </td>
                  <td>
                    <div class="cell">4.4</div>
                  </td>
                  <td>
                    <div class="cell">11070.4</div>
                  </td>
                  <td>
                    <div class="cell">515.1</div>
                  </td>
                  <td>
                    <div class="cell">17.2%</div>
                  </td>
                  <td>
                    <div class="cell">45723.5</div>
                  </td>
                  <td>
                    <div class="cell">2039.9</div>
                  </td>
                  <td>
                    <div class="cell">10.8%</div>
                  </td>
                  <td>
                    <div class="cell">63.8%</div>
                  </td>
                  <td>
                    <div class="cell">153162.7</div>
                  </td>
                  <td>
                    <div class="cell">5709.9</div>
                  </td>
                  <td>
                    <div class="cell">34.4%</div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">9.5%</div>
                  </td>
                  <td>
                    <div class="cell">79.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:22:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">110</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ccdc5c98a1f46ba521ccafd69424f310.png" alt="羲和" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">羲和</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">23</div>
                  </td>
                  <td>
                    <div class="cell">6</div>
                  </td>
                  <td>
                    <div class="cell">26%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">4.3</span>
                      <span class="kda2">0.6 / 2.1 / 5.7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.6</div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">5.7</div>
                  </td>
                  <td>
                    <div class="cell">6710.9</div>
                  </td>
                  <td>
                    <div class="cell">416.6</div>
                  </td>
                  <td>
                    <div class="cell">14.3%</div>
                  </td>
                  <td>
                    <div class="cell">21032.6</div>
                  </td>
                  <td>
                    <div class="cell">1266</div>
                  </td>
                  <td>
                    <div class="cell">8.1%</div>
                  </td>
                  <td>
                    <div class="cell">56.3%</div>
                  </td>
                  <td>
                    <div class="cell">77915.4</div>
                  </td>
                  <td>
                    <div class="cell">4190.6</div>
                  </td>
                  <td>
                    <div class="cell">22.2%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">2.5%</div>
                  </td>
                  <td>
                    <div class="cell">79.6%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:41</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">111</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/dfac89a287fb570f62dbc675d2efd526.png" alt="小七" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小七</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">31</div>
                  </td>
                  <td>
                    <div class="cell">8</div>
                  </td>
                  <td>
                    <div class="cell">25.8%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">1.9</span>
                      <span class="kda2">1.2 / 2.9 / 3.1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.2</div>
                  </td>
                  <td>
                    <div class="cell">2.9</div>
                  </td>
                  <td>
                    <div class="cell">3.1</div>
                  </td>
                  <td>
                    <div class="cell">7333.6</div>
                  </td>
                  <td>
                    <div class="cell">492.6</div>
                  </td>
                  <td>
                    <div class="cell">16.8%</div>
                  </td>
                  <td>
                    <div class="cell">38369.5</div>
                  </td>
                  <td>
                    <div class="cell">2495</div>
                  </td>
                  <td>
                    <div class="cell">14.8%</div>
                  </td>
                  <td>
                    <div class="cell">88.4%</div>
                  </td>
                  <td>
                    <div class="cell">90886.2</div>
                  </td>
                  <td>
                    <div class="cell">5230.9</div>
                  </td>
                  <td>
                    <div class="cell">26.6%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">7.8%</div>
                  </td>
                  <td>
                    <div class="cell">54.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:27</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">112</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0328bf8c0c2fc7e681a8a9604be62773.png" alt="景青" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">景青</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">8</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">25%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">1.7</span>
                      <span class="kda2">0.7 / 2.6 / 3.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">2.6</div>
                  </td>
                  <td>
                    <div class="cell">3.2</div>
                  </td>
                  <td>
                    <div class="cell">9192.6</div>
                  </td>
                  <td>
                    <div class="cell">521.6</div>
                  </td>
                  <td>
                    <div class="cell">18.1%</div>
                  </td>
                  <td>
                    <div class="cell">47009</div>
                  </td>
                  <td>
                    <div class="cell">2610.7</div>
                  </td>
                  <td>
                    <div class="cell">15.7%</div>
                  </td>
                  <td>
                    <div class="cell">85.1%</div>
                  </td>
                  <td>
                    <div class="cell">109482.3</div>
                  </td>
                  <td>
                    <div class="cell">5093.5</div>
                  </td>
                  <td>
                    <div class="cell">29.3%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">11.8%</div>
                  </td>
                  <td>
                    <div class="cell">60%</div>
                  </td>
                  <td>
                    <div class="cell">00:18:17</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">113</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/561864fc422e0fece270a52885fc8c74.png" alt="小羽" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小羽</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">37</div>
                  </td>
                  <td>
                    <div class="cell">9</div>
                  </td>
                  <td>
                    <div class="cell">24.3%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.4</span>
                      <span class="kda2">1.4 / 1.8 / 3.5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.4</div>
                  </td>
                  <td>
                    <div class="cell">1.8</div>
                  </td>
                  <td>
                    <div class="cell">3.5</div>
                  </td>
                  <td>
                    <div class="cell">8253.6</div>
                  </td>
                  <td>
                    <div class="cell">558.2</div>
                  </td>
                  <td>
                    <div class="cell">19.1%</div>
                  </td>
                  <td>
                    <div class="cell">82713.1</div>
                  </td>
                  <td>
                    <div class="cell">5268.1</div>
                  </td>
                  <td>
                    <div class="cell">30.5%</div>
                  </td>
                  <td>
                    <div class="cell">159.8%</div>
                  </td>
                  <td>
                    <div class="cell">46040.1</div>
                  </td>
                  <td>
                    <div class="cell">2727.1</div>
                  </td>
                  <td>
                    <div class="cell">13.9%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">4%</div>
                  </td>
                  <td>
                    <div class="cell">63.7%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:12</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">114</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2a64c518a7e4aeff978597d3011b75f4.png" alt="冰冰" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">冰冰</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">38</div>
                  </td>
                  <td>
                    <div class="cell">9</div>
                  </td>
                  <td>
                    <div class="cell">23.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2.7</span>
                      <span class="kda2">1.7 / 2.9 / 3.3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1.7</div>
                  </td>
                  <td>
                    <div class="cell">2.9</div>
                  </td>
                  <td>
                    <div class="cell">3.3</div>
                  </td>
                  <td>
                    <div class="cell">10681.2</div>
                  </td>
                  <td>
                    <div class="cell">728.8</div>
                  </td>
                  <td>
                    <div class="cell">24.9%</div>
                  </td>
                  <td>
                    <div class="cell">67204.8</div>
                  </td>
                  <td>
                    <div class="cell">4362.8</div>
                  </td>
                  <td>
                    <div class="cell">26.1%</div>
                  </td>
                  <td>
                    <div class="cell">104.4%</div>
                  </td>
                  <td>
                    <div class="cell">59638.9</div>
                  </td>
                  <td>
                    <div class="cell">3236.3</div>
                  </td>
                  <td>
                    <div class="cell">16.7%</div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">47.7%</div>
                  </td>
                  <td>
                    <div class="cell">67.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:09</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">115</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9087aab872e1deb4f2346058b31d35cc.png" alt="雨雨" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">雨雨</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">38</div>
                  </td>
                  <td>
                    <div class="cell">9</div>
                  </td>
                  <td>
                    <div class="cell">23.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.5</span>
                      <span class="kda2">0.7 / 2.1 / 4.6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.7</div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">4.6</div>
                  </td>
                  <td>
                    <div class="cell">6646.7</div>
                  </td>
                  <td>
                    <div class="cell">455.3</div>
                  </td>
                  <td>
                    <div class="cell">15.6%</div>
                  </td>
                  <td>
                    <div class="cell">28351.9</div>
                  </td>
                  <td>
                    <div class="cell">1875.3</div>
                  </td>
                  <td>
                    <div class="cell">11.4%</div>
                  </td>
                  <td>
                    <div class="cell">72.9%</div>
                  </td>
                  <td>
                    <div class="cell">76491.5</div>
                  </td>
                  <td>
                    <div class="cell">4546.1</div>
                  </td>
                  <td>
                    <div class="cell">23.1%</div>
                  </td>
                  <td>
                    <div class="cell">0.3</div>
                  </td>
                  <td>
                    <div class="cell">8.1%</div>
                  </td>
                  <td>
                    <div class="cell">71.2%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:09</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">116</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/395506052f0188bda91ff4934838cc93.png" alt="晚秋" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">晚秋</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">38</div>
                  </td>
                  <td>
                    <div class="cell">9</div>
                  </td>
                  <td>
                    <div class="cell">23.6%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2.3</span>
                      <span class="kda2">2.2 / 2.7 / 2.1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2.2</div>
                  </td>
                  <td>
                    <div class="cell">2.7</div>
                  </td>
                  <td>
                    <div class="cell">2.1</div>
                  </td>
                  <td>
                    <div class="cell">10290</div>
                  </td>
                  <td>
                    <div class="cell">700</div>
                  </td>
                  <td>
                    <div class="cell">23.9%</div>
                  </td>
                  <td>
                    <div class="cell">45639.5</div>
                  </td>
                  <td>
                    <div class="cell">2930.5</div>
                  </td>
                  <td>
                    <div class="cell">17.7%</div>
                  </td>
                  <td>
                    <div class="cell">74.8%</div>
                  </td>
                  <td>
                    <div class="cell">79488.3</div>
                  </td>
                  <td>
                    <div class="cell">4020.7</div>
                  </td>
                  <td>
                    <div class="cell">20.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.4</div>
                  </td>
                  <td>
                    <div class="cell">10.5%</div>
                  </td>
                  <td>
                    <div class="cell">61.1%</div>
                  </td>
                  <td>
                    <div class="cell">00:15:09</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">117</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fb08390611f294a193e26c089a9e9b46.png" alt="十三" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">十三</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">9</div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">22.2%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2.5</span>
                      <span class="kda2">0.5 / 2.8 / 5.2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">2.8</div>
                  </td>
                  <td>
                    <div class="cell">5.2</div>
                  </td>
                  <td>
                    <div class="cell">7531.7</div>
                  </td>
                  <td>
                    <div class="cell">465.8</div>
                  </td>
                  <td>
                    <div class="cell">15.5%</div>
                  </td>
                  <td>
                    <div class="cell">40578.2</div>
                  </td>
                  <td>
                    <div class="cell">2215.8</div>
                  </td>
                  <td>
                    <div class="cell">10.3%</div>
                  </td>
                  <td>
                    <div class="cell">67.2%</div>
                  </td>
                  <td>
                    <div class="cell">81096.2</div>
                  </td>
                  <td>
                    <div class="cell">4504.5</div>
                  </td>
                  <td>
                    <div class="cell">21.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.1</div>
                  </td>
                  <td>
                    <div class="cell">1.1%</div>
                  </td>
                  <td>
                    <div class="cell">71.3%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:57</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">118</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/c6c83917fb46d8108f687c23fb495959.png" alt="Zero" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Zero</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">7</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">14.2%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">3.2</span>
                      <span class="kda2">0.5 / 2.4 / 3.8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0.5</div>
                  </td>
                  <td>
                    <div class="cell">2.4</div>
                  </td>
                  <td>
                    <div class="cell">3.8</div>
                  </td>
                  <td>
                    <div class="cell">5616.8</div>
                  </td>
                  <td>
                    <div class="cell">419.5</div>
                  </td>
                  <td>
                    <div class="cell">14.7%</div>
                  </td>
                  <td>
                    <div class="cell">25468.2</div>
                  </td>
                  <td>
                    <div class="cell">1774.4</div>
                  </td>
                  <td>
                    <div class="cell">12.4%</div>
                  </td>
                  <td>
                    <div class="cell">85.1%</div>
                  </td>
                  <td>
                    <div class="cell">54692.5</div>
                  </td>
                  <td>
                    <div class="cell">3703.7</div>
                  </td>
                  <td>
                    <div class="cell">20.5%</div>
                  </td>
                  <td>
                    <div class="cell">0.2</div>
                  </td>
                  <td>
                    <div class="cell">6.3%</div>
                  </td>
                  <td>
                    <div class="cell">76.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:13:52</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">119</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/37c2f3e3d084f4baca8f2533c806c3c4.png" alt="秋沫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">秋沫</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2</span>
                      <span class="kda2">2 / 3 / 4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">9687</div>
                  </td>
                  <td>
                    <div class="cell">484</div>
                  </td>
                  <td>
                    <div class="cell">16.9%</div>
                  </td>
                  <td>
                    <div class="cell">95139</div>
                  </td>
                  <td>
                    <div class="cell">4557.6</div>
                  </td>
                  <td>
                    <div class="cell">25.2%</div>
                  </td>
                  <td>
                    <div class="cell">148.4%</div>
                  </td>
                  <td>
                    <div class="cell">58292</div>
                  </td>
                  <td>
                    <div class="cell">2702.1</div>
                  </td>
                  <td>
                    <div class="cell">13.1%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">66%</div>
                  </td>
                  <td>
                    <div class="cell">00:20:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">120</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8b0f78f3be042c62fb792803c864b2e2.png" alt="凌然" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">凌然</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">0.3</span>
                      <span class="kda2">0 / 3 / 1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">5717</div>
                  </td>
                  <td>
                    <div class="cell">357</div>
                  </td>
                  <td>
                    <div class="cell">13.6%</div>
                  </td>
                  <td>
                    <div class="cell">15805</div>
                  </td>
                  <td>
                    <div class="cell">960.7</div>
                  </td>
                  <td>
                    <div class="cell">9.3%</div>
                  </td>
                  <td>
                    <div class="cell">68.3%</div>
                  </td>
                  <td>
                    <div class="cell">79977</div>
                  </td>
                  <td>
                    <div class="cell">4515.1</div>
                  </td>
                  <td>
                    <div class="cell">32.7%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">100%</div>
                  </td>
                  <td>
                    <div class="cell">00:16:27</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">121</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/e85acf88871122e934de841cae2021e4.png" alt="可豪" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">可豪</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">0.8</span>
                      <span class="kda2">2 / 6 / 3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">6</div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">15300</div>
                  </td>
                  <td>
                    <div class="cell">765</div>
                  </td>
                  <td>
                    <div class="cell">26.8%</div>
                  </td>
                  <td>
                    <div class="cell">69835</div>
                  </td>
                  <td>
                    <div class="cell">3345.4</div>
                  </td>
                  <td>
                    <div class="cell">18.5%</div>
                  </td>
                  <td>
                    <div class="cell">69%</div>
                  </td>
                  <td>
                    <div class="cell">135219</div>
                  </td>
                  <td>
                    <div class="cell">4490.9</div>
                  </td>
                  <td>
                    <div class="cell">21.7%</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">20%</div>
                  </td>
                  <td>
                    <div class="cell">55%</div>
                  </td>
                  <td>
                    <div class="cell">00:20:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">122</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/54deb50c5315d2e18ef58fbeaf1f1778.png" alt="Best" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Best</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">2</span>
                      <span class="kda2">1 / 5 / 9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">9</div>
                  </td>
                  <td>
                    <div class="cell">8074</div>
                  </td>
                  <td>
                    <div class="cell">403</div>
                  </td>
                  <td>
                    <div class="cell">13.1%</div>
                  </td>
                  <td>
                    <div class="cell">30368</div>
                  </td>
                  <td>
                    <div class="cell">1459</div>
                  </td>
                  <td>
                    <div class="cell">7.6%</div>
                  </td>
                  <td>
                    <div class="cell">58.4%</div>
                  </td>
                  <td>
                    <div class="cell">131263</div>
                  </td>
                  <td>
                    <div class="cell">5888.8</div>
                  </td>
                  <td>
                    <div class="cell">26.4%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">71%</div>
                  </td>
                  <td>
                    <div class="cell">00:20:49</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">123</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5b4d1e1ddbb7294001b2120b5aa7662c.png" alt="小求" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小求</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">0.8</span>
                      <span class="kda2">1 / 5 / 3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">5</div>
                  </td>
                  <td>
                    <div class="cell">3</div>
                  </td>
                  <td>
                    <div class="cell">6918</div>
                  </td>
                  <td>
                    <div class="cell">532</div>
                  </td>
                  <td>
                    <div class="cell">18.4%</div>
                  </td>
                  <td>
                    <div class="cell">38549</div>
                  </td>
                  <td>
                    <div class="cell">2900.3</div>
                  </td>
                  <td>
                    <div class="cell">18.4%</div>
                  </td>
                  <td>
                    <div class="cell">100%</div>
                  </td>
                  <td>
                    <div class="cell">48216</div>
                  </td>
                  <td>
                    <div class="cell">3439.6</div>
                  </td>
                  <td>
                    <div class="cell">15.8%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">50%</div>
                  </td>
                  <td>
                    <div class="cell">00:13:18</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">124</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7cc6c9642247d873cdee6a140a3beebf.png" alt="话诗" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">话诗</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">2</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">0.7</span>
                      <span class="kda2">0 / 1.5 / 1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">1.5</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">5851.5</div>
                  </td>
                  <td>
                    <div class="cell">439.5</div>
                  </td>
                  <td>
                    <div class="cell">16.4%</div>
                  </td>
                  <td>
                    <div class="cell">55907.5</div>
                  </td>
                  <td>
                    <div class="cell">4098.7</div>
                  </td>
                  <td>
                    <div class="cell">31.4%</div>
                  </td>
                  <td>
                    <div class="cell">189.3%</div>
                  </td>
                  <td>
                    <div class="cell">26927.5</div>
                  </td>
                  <td>
                    <div class="cell">1857.2</div>
                  </td>
                  <td>
                    <div class="cell">10.4%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">66.5%</div>
                  </td>
                  <td>
                    <div class="cell">00:13:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">125</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8f3b2498ca11603c682a4ce871587728.png" alt="傲神" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">傲神</span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">
                      <span class="kda1">0.3</span>
                      <span class="kda2">0 / 4 / 1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">4</div>
                  </td>
                  <td>
                    <div class="cell">1</div>
                  </td>
                  <td>
                    <div class="cell">6248</div>
                  </td>
                  <td>
                    <div class="cell">624</div>
                  </td>
                  <td>
                    <div class="cell">22.4%</div>
                  </td>
                  <td>
                    <div class="cell">22290</div>
                  </td>
                  <td>
                    <div class="cell">2067</div>
                  </td>
                  <td>
                    <div class="cell">14.5%</div>
                  </td>
                  <td>
                    <div class="cell">64.7%</div>
                  </td>
                  <td>
                    <div class="cell">55877</div>
                  </td>
                  <td>
                    <div class="cell">3929.5</div>
                  </td>
                  <td>
                    <div class="cell">19.3%</div>
                  </td>
                  <td>
                    <div class="cell">0</div>
                  </td>
                  <td>
                    <div class="cell">0%</div>
                  </td>
                  <td>
                    <div class="cell">20%</div>
                  </td>
                  <td>
                    <div class="cell">00:10:47</div>
                  </td>
                </tr></tbody>
            </table></div><div class="c-table__fixed-right-patch" style="width: 9px; height: 43px;"></div> <div class="c-table__fixed c-table__fixed--shadow" style="width: 233px; height: 531.4px;"> <div class="c-table__fixed-header-wrapper"><table cellspacing="0" cellpadding="0" border="0" role="c-table1" data-height="542" class="c-table__header" style="width: 2346px;">
              <colgroup id="colgroup"><col name="" width="100"><col name="" width="133"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="113"></colgroup>
              <thead>
                <tr id="table-header">
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">排名</div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p pop-team">
                        选手
                        <img class="sx-icon" src="//game.gtimg.cn/images/yxzj/matchdata/sx.png" width="11px" height="12px" alt="" srcset="">
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        比赛场次 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        胜场 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        胜率 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均KDA <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均击杀数 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均死亡数 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均助攻数 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均经济 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        分均经济 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        经济占比 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均伤害 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        分均伤害 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        伤害占比 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        伤害转化率 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均承伤 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        分均承伤 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        承伤占比 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均推塔数 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        推搭占比 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        参团率 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                  <th colspan="1" rowspan="1">
                    <div class="h-item cell">
                      <div class="h-item-p">
                        场均比赛时长 <span class="triangle-up"></span>
                        <span class="triangle-down"></span>
                      </div>
                    </div>
                  </th>
                </tr>
              </thead>
              
            </table></div><div class="c-table__fixed-body-wrapper" style="max-height: 488.4px; top: 43px;"> <table cellspacing="0" cellpadding="0" border="0" role="c-table1" data-height="542" class="c-table__body" style="width: 2346px; margin-top: 0px;">
              <colgroup id="colgroup"><col name="" width="100"><col name="" width="133"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="100"><col name="" width="113"></colgroup>
              
              <tbody><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">1</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/38e591cf1ed8efa83ea56f34bbb88af7.png" alt="花月" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">花月</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">100%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">9</span>
                      <span class="kda2">5 / 1 / 4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7554</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">755</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">49291</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4518.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">103.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23929</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1832.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:10:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">2</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/c5f03a87d36aef19a400d1d09365a35a.png" alt="无铭" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">无铭</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">100%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">11.5</span>
                      <span class="kda2">0 / 1 / 11.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6248.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">475</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19384.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1341.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50835.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3075</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">77.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:14:26</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">3</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/b3dcd48a50cc8b4fd2a3479614157382.png" alt="自渡" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">自渡</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">100%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">8</span>
                      <span class="kda2">1 / 0 / 7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6322</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">632</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31683</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2904.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51490</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4251.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">34.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:10:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">4</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/de4b9d54a1c9bfdffea83e29080e0aa9.png" alt="归期" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">归期</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">83.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.3</span>
                      <span class="kda2">2.5 / 1.3 / 4.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9835.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">649.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51265.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3202</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72338.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3703.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:28</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">5</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/3131a3a52761b06dcb89c5ab7f66e52e.png" alt="风劫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">风劫</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">80%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.2</span>
                      <span class="kda2">3.6 / 2.6 / 5.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13112.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">743</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">97282.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5247.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">112.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70503</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2951.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">73.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:18:27</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">6</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/63c9ee50a54d077c0d7af79e59c0b7cc.png" alt="月色" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">月色</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.1</span>
                      <span class="kda2">0.5 / 1.6 / 6.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10407.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">603.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">116158.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6026.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">148.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46715.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2136.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">7</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a2a8b6d77f5f3f921406de464abe3216.png" alt="钟意" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">钟意</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">6.2</span>
                      <span class="kda2">3 / 1.7 / 5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12402.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">743.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57220.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3316.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">97741.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3933.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">8</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/60d74420e4df0e080b29c307368dacc6.png" alt="帆帆" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">帆帆</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">60</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">7.1</span>
                      <span class="kda2">0.8 / 1.2 / 8.1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7110.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">454.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38638.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2241.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71765.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3672.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:17</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">9</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ca303f0f42b7ce8619dc433c3ed69b23.png" alt="妖刀" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">妖刀</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">6</span>
                      <span class="kda2">3.2 / 1.4 / 4.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11987.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">756.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88852.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5265.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">107.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62970.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2837.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">10</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a5f65ff7a7665af4718b90f48b76789c.png" alt="小胖" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小胖</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">44</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.4</span>
                      <span class="kda2">2.7 / 1.6 / 4.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11793.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">750</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64148.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3941.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">84.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">97764</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4186.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:18</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">11</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/3109a021ad37fbc536c5dc51405b8654.png" alt="向鱼" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">向鱼</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">6.2</span>
                      <span class="kda2">2.2 / 1.2 / 5.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8693.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">554.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">92274.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5483.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">151.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38256.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2009.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:13</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">12</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5cd022c1258f158b76b9856a9fb52389.png" alt="Fly" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Fly</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">1.9 / 1.7 / 4.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9333.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">591.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53718</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3201.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">83.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">92917.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4485.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">59.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:29</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">13</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/36ee63cce8a0061c6c2d887f2ebbe622.png" alt="一笙" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">一笙</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">6.3</span>
                      <span class="kda2">0.9 / 1.5 / 7.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7272.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">448.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">34947.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1997.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">92714</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4731.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">14</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/34b847d9d4acf1fb377d2b4fd50af251.png" alt="誓约" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">誓约</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4</span>
                      <span class="kda2">2.1 / 2 / 3.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9791.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">620.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">44036.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2672.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85698.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4263.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:29</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">15</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2a4ea3d4cca408009c033f13509ed748.png" alt="一门" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">一门</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">6.7</span>
                      <span class="kda2">0.6 / 1.2 / 7.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7622.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">483.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26492.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1567.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79300.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3947.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:33</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">16</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/b762a5abeaa00cd1da6fdd77c490161b.png" alt="暖阳（林恒）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">暖阳（林恒）</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.4</span>
                      <span class="kda2">2.8 / 1.9 / 4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12184.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">740</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55187.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3135.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">93275.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3787.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">17</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8d45528e4577c5ecb17f2aa37a78dde4.png" alt="梓墨" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">梓墨</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.5</span>
                      <span class="kda2">1.7 / 1.8 / 4.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9598.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">584.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51998.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3007.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">92.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">102158.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4897.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">18</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/6031efec47f5ad279253f962635a0ecc.png" alt="星宇" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">星宇</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.9</span>
                      <span class="kda2">0.5 / 1.4 / 7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7515.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">458.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24288.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1440.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85062.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4222.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">74.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">19</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/14541912d6728e93c66a42a23bf32cfe.png" alt="花卷" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">花卷</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.2</span>
                      <span class="kda2">2 / 1.5 / 4.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9345.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">563.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88657.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5068.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">157.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43114.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2173.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">20</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2109f8770f35fe7af93e8e2866bb393d.png" alt="乔兮" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">乔兮</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">2.8 / 1.6 / 3.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12617.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">766.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">86342.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4872.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">113%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62626.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2779.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">21</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ce86be8444a4587fd6a5201d2a1fb4ed.png" alt="不然" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">不然</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">3.2 / 1.7 / 4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12731.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">782.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51794.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3035.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">83303.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3347.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">22</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/eb48fec336a3035bbaff57bda95d65c5.png" alt="阿豆（蒋涛）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">阿豆（蒋涛）</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.8</span>
                      <span class="kda2">0.5 / 1.7 / 7.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7261.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">448</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">32722.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1838.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75589.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3818</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">23</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/cd3b48b9f8fe8e96abab73573cd83965.png" alt="风箫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">风箫</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.3</span>
                      <span class="kda2">2.5 / 2.1 / 4.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12308.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">753.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">90852.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5190.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">118.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64742.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2921.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">24</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/42c878fddfd0d188f155b6c497e0c5c8.png" alt="清清" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">清清</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">2.2 / 1.7 / 4.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9600.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">587.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52293.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3049.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">91.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">94515.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4625.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">25</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/6d899f90a771b5aef541a5c548363764.png" alt="九尾" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">九尾</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.4</span>
                      <span class="kda2">1.7 / 1.5 / 5.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9142.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">563.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">84601.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4952.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">150.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40878.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2058.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">26</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5933ec732ac62f3a76813239d4217ae4.png" alt="早点" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">早点</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">87</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.5</span>
                      <span class="kda2">1.4 / 1.2 / 5.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8944</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">536.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">97258.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5396</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">163.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40811.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2015</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:20</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">27</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/e1906088d0ae9e9d2c0c2ae4933748fd.png" alt="未央" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">未央</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">54.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">2.3 / 1.7 / 3.1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11551.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">723.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">44780.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2686.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">80753.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3395.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">28</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/c887c33254a27e4b6990f4c52f33d9df.png" alt="Cat" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Cat</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">54.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.3</span>
                      <span class="kda2">0.4 / 2.2 / 6.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7336.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">440.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28751.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1629.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">95358.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4800.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:18</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">29</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/1dc617e6ee4edc26f834b370dd0fb879.png" alt="绝意" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">绝意</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">54.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.2</span>
                      <span class="kda2">2.9 / 1.7 / 3.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12438</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">747</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88220.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4924.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">108.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">60284.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2620.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:16</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">30</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8bc3ee8cf44809ac7f6cf9f3db18bfbd.png" alt="赤辰" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">赤辰</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.8</span>
                      <span class="kda2">1.9 / 2 / 4.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11582.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">696.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53945.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3113.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">98703.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4235.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:15</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">31</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a9d72875be343eaa9ece04de5c15c04d.png" alt="小落" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小落</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2.2 / 2.1 / 4.1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10475.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">634.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57812.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3309.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">87.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">92309.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4358.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:15</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">32</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/47426b6d08ba1b9eb5d9ae750dba2e1d.png" alt="清融" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">清融</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">78</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.8</span>
                      <span class="kda2">2.1 / 1.8 / 6.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9154.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">561.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">100653.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5842.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">168%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48426.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2435.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">74.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">33</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fabf19fb0188947220f55e0a309fe101.png" alt="子阳" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">子阳</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">78</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">6.6</span>
                      <span class="kda2">0.7 / 1.7 / 8.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7243.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">442.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">32841.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1869.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65748.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3362.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">80.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">34</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/11872ff2e53bc3fc33d028cc9daf749d.png" alt="花海（罗思源）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">花海（罗思源）</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">78</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.1</span>
                      <span class="kda2">3.3 / 2 / 4.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12672.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">774.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55614.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3303.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89348.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3706.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">35</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ade9f2ceee080e3d63dad74b30d252d6.png" alt="坦然（孙麟威）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">坦然（孙麟威）</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">78</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">1.9 / 1.9 / 5.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9101.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">565.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">49505.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2969.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">95057.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4675</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">36</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/f6bfc9197e6dc0dfe8ffcac26544c8b8.png" alt="言梦" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">言梦</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.4</span>
                      <span class="kda2">0.5 / 1.8 / 7.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6949.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">414.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31599.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1789.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">83913.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4256.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">77.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">37</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5ce064c461a25bc1594d17a707e975a4.png" alt="今屿" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">今屿</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.6</span>
                      <span class="kda2">2.4 / 1.8 / 3.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12610.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">775</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57800.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3322.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">94098.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3853.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:02</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">38</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d650a1c4a421465ea1324f85691432cd.png" alt="傲寒" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">傲寒</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">77</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">41</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2.4 / 1.9 / 3.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12076.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">755.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85885.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5049.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">112.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58655.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2657.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:15</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">39</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/c9bd1afee0b367315b98a831f1389c99.png" alt="铃铛" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">铃铛</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.5</span>
                      <span class="kda2">1.5 / 1.3 / 4.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9489.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">608.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">94245.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5577.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">159.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42293.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2178.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:19</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">40</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9573fcc4b7d8805532f762ed6785edaa.png" alt="鹏鹏" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">鹏鹏</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">91</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2.5 / 1.9 / 3.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12071.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">730.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">49479.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2847.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">90862.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3734.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">41</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/faac4faa28d92bddc3e143afdd057921.png" alt="阿改" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">阿改</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">91</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.4</span>
                      <span class="kda2">0.6 / 1.4 / 6.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7505.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">454.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26501.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1503.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">59.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70767.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3612.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">42</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/03d1c607fdee6e1f4526d9568ae165d8.png" alt="青枫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">青枫</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">91</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">1.5 / 1.4 / 4.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9083.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">548.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85344.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4866.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">161.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43714.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2241.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">43</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/37f7d0359012b5e38e44202f686f271e.png" alt="百兽" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">百兽</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">91</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">1.3 / 1.9 / 4.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9178.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">557.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">39553</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2296.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">90759.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4459.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">44</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9e2b874427ddb2f23452748c340b266a.png" alt="梦岚" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">梦岚</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">91</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.9</span>
                      <span class="kda2">2.5 / 1.6 / 3.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12567.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">760</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">87991.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5021.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">120.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62877.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2775</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">73.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:51</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">45</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/f50df692e9332268fc0461bc15dc09fb.png" alt="易峥" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">易峥</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">73</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5</span>
                      <span class="kda2">2.9 / 2 / 4.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12098.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">742.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88326.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5023.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">109.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63834</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2841.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">46</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0588a8dd00258118b5cf1fcb610556af.png" alt="无畏" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">无畏</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">1.8 / 1.9 / 3.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11187.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">709.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52654</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3125.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">94422.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4259.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:04</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">47</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0bc827584405baaceb878f98453ff248.png" alt="玄影" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">玄影</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">2.2 / 2.1 / 3.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12667.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">774.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47321.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2701.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82429.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3281.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">48</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d6d8526e6342b92e8d01233ccbd5df94.png" alt="Roc" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Roc</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.6</span>
                      <span class="kda2">3 / 1.7 / 3.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12799.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">775.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">86479.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4934.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">112.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62965.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2822.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">49</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/73a963d37fbc9af5d839d39b2075874b.png" alt="柠栀" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">柠栀</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.3</span>
                      <span class="kda2">1.5 / 1.6 / 4.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9119.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">551.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">44119.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2576</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">83.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">102274.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5145.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">50</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fd5ccf7df062feca229a9d5f47fccd2d.png" alt="Ming" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Ming</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">51.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.8</span>
                      <span class="kda2">1.7 / 1.6 / 5.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9493.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">580.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">93480.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5428.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">167.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45783.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2353.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">73.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">51</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/beb7d3d855278db7fc92dbd7952432a8.png" alt="一曲" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">一曲</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">35</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.1</span>
                      <span class="kda2">1.3 / 1.2 / 4.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8923.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">532</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">91323.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5106.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">168.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43375.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2171.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">52</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/28b0c1c86bba11d3777e41deef12d105.png" alt="啊泽" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">啊泽</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">35</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.8</span>
                      <span class="kda2">1.4 / 2 / 4.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9095.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">539.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42890</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2419.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">77.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">103015.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5071.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">53</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a53645eda564019b8c18572522170a01.png" alt="小A" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小A</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">35</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.6</span>
                      <span class="kda2">0.6 / 1.4 / 6.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7478.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">444</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">33618.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1917</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">73.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81892.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4158.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">54</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/e97d18a7b189150074b0bf345e748842.png" alt="小玖" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小玖</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">35</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.4</span>
                      <span class="kda2">3 / 1.6 / 3.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13365.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">791.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">86252.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4783.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">107.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58585.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2597.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:25</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">55</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2ee59d91feade6c3b6e42e74d289ec44.png" alt="久酷" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">久酷</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">91</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.5</span>
                      <span class="kda2">0.7 / 1.2 / 6.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6839.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">435.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26003.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1587.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">74120.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3956.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:03</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">56</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/831ad155e862a0da8c048c80ae873aaf.png" alt="小崽" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小崽</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">6.3</span>
                      <span class="kda2">0 / 0.7 / 6.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7121.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">457.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21181.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1319</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56979.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3123.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">93.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">57</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/3c367d6e5ca7a2b79a685f05a1eb8589.png" alt="An" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">An</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">1.2 / 2.5 / 5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7786</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">460.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">41054.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2335.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">93.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">139448.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6842.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">36.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:38</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">58</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/12d0811490492112e295bd0409324003.png" alt="江城" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">江城</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.5</span>
                      <span class="kda2">1.7 / 1.7 / 4.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11990.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">717</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63027</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3721.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">97.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53795</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2666.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">54.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:03</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">59</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d7d43bc95a455c4acdc95c1a498e7ef2.png" alt="晨风" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">晨风</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.7</span>
                      <span class="kda2">0.8 / 1.1 / 5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7661.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">516.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82041</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5394.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">179.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40496.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2315.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">60</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0d8d108ab2c3a10240430bbecce51e2f.png" alt="一诺（徐必成）" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">一诺（徐必成）</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">2.4 / 1.6 / 3.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12704.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">794</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81580.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4892.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">110.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">59199.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2715.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">44.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">61</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7115f6074ac26e71cc3c750cdcd15ae0.png" alt="忆安" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">忆安</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3</span>
                      <span class="kda2">1.3 / 2 / 3.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9023.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">561.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40360.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2403.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">86828.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4488</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">62</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d8f8ea8bf065993c5a039129c836e113.png" alt="长生" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">长生</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.4</span>
                      <span class="kda2">1.5 / 1.3 / 4.1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9100.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">567.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">95967.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5690.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">32.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">180.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">44238.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2360.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">63</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/dee0b1d9815975dc77abc3f6beee2cf6.png" alt="夏竹" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">夏竹</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.4</span>
                      <span class="kda2">0.4 / 1.8 / 6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7141.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">448.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27405.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1619.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">74777.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3996.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">80.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:31</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">64</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/4d3742c88bdd31560a43ff09ab5e2783.png" alt="冰然" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">冰然</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">35</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2.9</span>
                      <span class="kda2">1.9 / 2.5 / 3.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12012.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">706.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">49846.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2739.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">90473.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3605.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">60.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:47</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">65</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/eca2317db974f302eeeadb7718d4002c.png" alt="556" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">556</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.8</span>
                      <span class="kda2">0.6 / 1.9 / 6.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7476.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">439.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26606.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1422</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">87389</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4331.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">80.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:44</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">66</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/276858cb556f317c2b5ba8735800da28.png" alt="千世" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">千世</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4</span>
                      <span class="kda2">1.2 / 2 / 4.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9408.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">546.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">103696.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5553.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">174.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53455.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2607.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:48</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">67</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/6476ebef7ce9703c7d6a9eef1973b92c.png" alt="佩恩" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">佩恩</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.5</span>
                      <span class="kda2">2.7 / 1.4 / 3.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13412.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">779.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">90827.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4904.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">109.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63805.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2742</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:48</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">68</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/988d4be506b65f5de79bd2598d2baa2c.png" alt="爱思" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">爱思</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">6.1</span>
                      <span class="kda2">1 / 1.6 / 5.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7075.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">455</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26492.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1598.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81607</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4213.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:22</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">69</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a94ae4eeea3d9a98a5bf286c302e26f2.png" alt="小夜" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小夜</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">32</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.3</span>
                      <span class="kda2">2.1 / 1.9 / 3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12134.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">735.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52653.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3050.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">77.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85911.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3612.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">70</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/b56f5210f974dc282e71b4ed4b79d16a.png" alt="梓轩" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">梓轩</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">1.5 / 2.1 / 3.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8352.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">510.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">39159.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2318.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88443.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4521.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">71</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/04300319226899b16d9e7ade24d6e314.png" alt="以然" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">以然</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">52</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.4</span>
                      <span class="kda2">2 / 2.2 / 3.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12145.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">699.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50132.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2785</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85193.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3563</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">60.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">72</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d9c3b3c3ef3da4614fb778678ce840a2.png" alt="仙语" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">仙语</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">39</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.3</span>
                      <span class="kda2">1.8 / 2.4 / 3.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10045.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">575.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50901.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2785.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">86%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">96918.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4739.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">73</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/cca0e32562495551f243e1f92274e547.png" alt="小久" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小久</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5</span>
                      <span class="kda2">2.9 / 1.5 / 3.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12914.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">778.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">92009.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5234.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">115.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62119.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2807.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">74</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/47767bd2507a965cf4c38eabb91b8e9a.png" alt="久凡" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">久凡</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.8</span>
                      <span class="kda2">0.7 / 2 / 7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7598.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">461.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27152.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1561.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">93363.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4784.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">78.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">75</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/e9a35c0f92bd12e7ca50af991b5b59a4.png" alt="迷途" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">迷途</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2 / 2.2 / 4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11831.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">722.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48689.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2826.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88897.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3753.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">60.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">76</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8087dfbdf220f4dbf1c2d8ced3a5faed.png" alt="阿怪" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">阿怪</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.8</span>
                      <span class="kda2">2 / 2.6 / 4.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9188.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">555.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47240.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2764.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">101014.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4993.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">77</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/98b7d418ea608c3f940042b2c9318285.png" alt="笑影" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">笑影</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">1.3 / 1.8 / 4.1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8820.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">530.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">83904</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4822.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">164.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">49334.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2620.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:59</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">78</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/48a2ded453710c49b80989954dea1922.png" alt="情缘" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">情缘</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5</span>
                      <span class="kda2">1.7 / 1.5 / 5.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9166</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">553.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">100121.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5600.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">171.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45333.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2390.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:07</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">79</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fbe28816578b5b5dcb758ce547ac5818.png" alt="晚星" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">晚星</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">2.2 / 2 / 3.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12445.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">705.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57792.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3160.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">109936.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4586.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:18:08</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">80</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/98e4fa9e72db8735209227f4f121b562.png" alt="东方" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">东方</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.4</span>
                      <span class="kda2">1.9 / 2 / 3.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8752.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">566</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45276.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2778.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">87612</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4588</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:46</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">81</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7c19f73653eebeb163b7861ce9961e6a.png" alt="花云" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">花云</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">2.5 / 1.5 / 2.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12185.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">734.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82239.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4596.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">112%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56037.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2579.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">82</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/f019291412bf15426a5cbc39afd18591.png" alt="冰尘" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">冰尘</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">5.5</span>
                      <span class="kda2">0.5 / 1.3 / 6.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7302.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">428.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25182</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1408.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">90739</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4575</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">78.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">83</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9b3cef40ec005b398e2e6c78d733eb70.png" alt="苏沫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">苏沫</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.8</span>
                      <span class="kda2">1.6 / 2 / 4.1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9244.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">544.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37527</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2141</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">102027.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4994</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">84</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/47e30493ec817b2c34cf5c82f5b58d9c.png" alt="幕色" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">幕色</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.6</span>
                      <span class="kda2">1.3 / 1.5 / 4.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8954.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">523.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">101989.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5631.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">33%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">189.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45423.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2326.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">85</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fcdd4da0c20422cebc71a35df5a20bfb.png" alt="蓝桉" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">蓝桉</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">2.5 / 1.5 / 3.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13367.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">778.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">93654.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5127.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">113.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67230.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3028.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:37</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">86</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/b01cb2ce26a07a06bc519a6ff847b59a.png" alt="星痕" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">星痕</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.3</span>
                      <span class="kda2">1.4 / 2 / 3.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8381.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">549.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76101.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4600.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">139.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">49449.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2787.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:36</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">87</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/92b982171748e8d0e08e29d817e4d164.png" alt="不弃" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">不弃</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">44.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">0.3 / 1.5 / 5.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7186.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">435</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25157.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1437.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">59.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">83956.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4356.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">77.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:54</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">88</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8ae1b3437b077613bd309aa15bbee728.png" alt="酷偕" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">酷偕</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">32</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.5</span>
                      <span class="kda2">1.3 / 1.9 / 3.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8675.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">547.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">43129.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2621</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">86.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">93694.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4947.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:13</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">89</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/1e8f31a72ea4d38212bdbf473c55ee9e.png" alt="梓凡" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">梓凡</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">3.2 / 2.8 / 3.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14170.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">762.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53272.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2773.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">84873.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3307.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:18:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">90</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/926ae6a4e63c48e1ec989ae0df604f0f.png" alt="顾兴" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">顾兴</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.5</span>
                      <span class="kda2">2 / 1.3 / 2.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11787.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">739.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45685.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2840.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82417.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3635.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:28</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">91</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5def77d9d240b0e5fd44cdf3ed78f41d.png" alt="情川" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">情川</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">41.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.5</span>
                      <span class="kda2">1 / 1.6 / 3.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8286.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">540.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">35620.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2286.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">74.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">93415.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4851.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:13</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">92</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/84ebf5c426b75033b4e1df73fbe5cf2a.png" alt="决明" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">决明</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.6</span>
                      <span class="kda2">1 / 1.3 / 3.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8862.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">536.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">99848.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5459.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">177.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42921.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2230.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:60</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">93</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7bcd79d0e0a980c3b116ed2b2a27b0d7.png" alt="林一" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">林一</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2.7</span>
                      <span class="kda2">1.8 / 1.8 / 2.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12833.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">808.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">41055</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2481.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76414.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3165.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">57.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:23</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">94</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/cdd628c5a4e9fffa672d0df64fb110da.png" alt="灵梦" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">灵梦</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.7</span>
                      <span class="kda2">1.3 / 1.5 / 4.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9069.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">565.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88761</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5120.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">158.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45148.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2363</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:38</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">95</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9f4f7b1b8aefb81a33a98c843d4fc3cc.png" alt="九月" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">九月</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.2</span>
                      <span class="kda2">3 / 1.7 / 2.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11360.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">712.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45366.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2685.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">77803.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3146.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:38</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">96</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/43b28d3e73ace965ee0bd5561258bace.png" alt="秀豆" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">秀豆</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4</span>
                      <span class="kda2">2.3 / 1.4 / 3.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12141.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">756.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89104.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5230.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">121.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55297.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2594</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:38</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">97</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/a21c30d04be583356cb6e8cffb89529e.png" alt="稚念" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">稚念</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">39.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.8</span>
                      <span class="kda2">0.4 / 1.3 / 5.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7109.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">431</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28453.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1525.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">59.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71258.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3641.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">78.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">98</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0cdf1dd856cab1fd5475977c82f9d658.png" alt="钎城" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">钎城</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">39.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.1</span>
                      <span class="kda2">1.7 / 1.1 / 2.9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12387.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">734.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88089.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4777</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">110.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">59939.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2617.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">99</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7711821e098a9853ce69bd6903b907cc.png" alt="小义" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小义</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">39.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.9</span>
                      <span class="kda2">2.7 / 1.9 / 2.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12769.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">764.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55972.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3209</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">74.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">83710.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3347.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">74.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">100</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/268ab209ef89f2aa4bd81b452e9bac26.png" alt="文帝" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">文帝</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.2</span>
                      <span class="kda2">1.1 / 1.1 / 3.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9161.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">529.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">113626</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5887.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">33.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">187%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42583.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2155.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:17:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">101</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0af445ace86a94640448d1b6cd810d05.png" alt="小椿" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小椿</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">34.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2.7</span>
                      <span class="kda2">1.9 / 2.2 / 2.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11862</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">750.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42474.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2650.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">62.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68462</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3080.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:32</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">102</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ab0ad160d0a21ab9186176d1b819da39.png" alt="季节" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">季节</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">33.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2.5</span>
                      <span class="kda2">2 / 2.6 / 4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10830.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">812.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53605.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3779</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81531</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4440.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">53.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:13:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">103</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/d0f5e9f6fee630bf5519cae6d1da095a.png" alt="无上" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">无上</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">33.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2</span>
                      <span class="kda2">0 / 1.6 / 3.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5697</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">460</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23217</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1751.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89203</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6178.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">32.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:13:06</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">104</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/573ca193e4c832d81953b2245713471e.png" alt="小磊" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小磊</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">32.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4</span>
                      <span class="kda2">0.7 / 2 / 5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6608.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">426.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24547.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1518.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">75094.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4007.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:55</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">105</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2ddaf7b8d271e9ed87a458ec48c946bc.png" alt="小年" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小年</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.2</span>
                      <span class="kda2">2 / 2.1 / 3.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11611.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">737.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85532.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5076.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">118.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65648.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3271.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:10</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">106</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/f9506254c198d2d0db3fff0527893892.png" alt="末将" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">末将</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.7</span>
                      <span class="kda2">1.6 / 1.6 / 3.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8605.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">547.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89828.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5165.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">159.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">42484.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2472.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:10</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">107</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8ee4721ed5162f123e89bcc47a30d0e3.png" alt="Qy" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Qy</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">34</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.3</span>
                      <span class="kda2">2.2 / 2 / 2.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11472.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">717.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">49381.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2865.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">70.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">89982.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4057.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">65.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:22</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">108</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/4d6d01c683acf5694978910995f9a3eb.png" alt="背影" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">背影</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">34</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.4</span>
                      <span class="kda2">1 / 2.2 / 4.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8263.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">515.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">39122.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2321.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">80.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">95159</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5139.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">27%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:26</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">109</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/35faba2f440631c6314f9aae67c25f83.png" alt="杰杰" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">杰杰</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.1</span>
                      <span class="kda2">0.7 / 2.5 / 4.4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11070.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">515.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45723.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2039.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">153162.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5709.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">34.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:22:21</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">110</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/ccdc5c98a1f46ba521ccafd69424f310.png" alt="羲和" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">羲和</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">4.3</span>
                      <span class="kda2">0.6 / 2.1 / 5.7</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6710.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">416.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21032.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1266</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">56.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">77915.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4190.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:41</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">111</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/dfac89a287fb570f62dbc675d2efd526.png" alt="小七" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小七</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">1.9</span>
                      <span class="kda2">1.2 / 2.9 / 3.1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7333.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">492.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38369.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2495</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">88.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">90886.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5230.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">54.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:27</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">112</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/0328bf8c0c2fc7e681a8a9604be62773.png" alt="景青" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">景青</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">1.7</span>
                      <span class="kda2">0.7 / 2.6 / 3.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9192.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">521.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47009</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2610.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">109482.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5093.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">29.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">60%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:18:17</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">113</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/561864fc422e0fece270a52885fc8c74.png" alt="小羽" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小羽</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">37</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.4</span>
                      <span class="kda2">1.4 / 1.8 / 3.5</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8253.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">558.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">82713.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5268.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">159.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">46040.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2727.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">63.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:12</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">114</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/2a64c518a7e4aeff978597d3011b75f4.png" alt="冰冰" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">冰冰</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2.7</span>
                      <span class="kda2">1.7 / 2.9 / 3.3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10681.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">728.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">24.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67204.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4362.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">104.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">59638.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3236.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">47.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:09</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">115</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/9087aab872e1deb4f2346058b31d35cc.png" alt="雨雨" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">雨雨</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.5</span>
                      <span class="kda2">0.7 / 2.1 / 4.6</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6646.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">455.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">28351.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1875.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">11.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">72.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76491.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4546.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:09</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">116</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/395506052f0188bda91ff4934838cc93.png" alt="晚秋" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">晚秋</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2.3</span>
                      <span class="kda2">2.2 / 2.7 / 2.1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10290</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">700</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">23.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">45639.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2930.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">17.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">74.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79488.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4020.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">61.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:15:09</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">117</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/fb08390611f294a193e26c089a9e9b46.png" alt="十三" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">十三</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2.5</span>
                      <span class="kda2">0.5 / 2.8 / 5.2</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7531.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">465.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">40578.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2215.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">67.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">81096.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4504.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:57</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">118</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/c6c83917fb46d8108f687c23fb495959.png" alt="Zero" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Zero</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">3.2</span>
                      <span class="kda2">0.5 / 2.4 / 3.8</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5616.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">419.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25468.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1774.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">12.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">85.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">54692.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3703.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">76.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:13:52</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">119</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/37c2f3e3d084f4baca8f2533c806c3c4.png" alt="秋沫" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">秋沫</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2</span>
                      <span class="kda2">2 / 3 / 4</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9687</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">484</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.9%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">95139</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4557.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">25.2%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">148.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58292</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2702.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:20:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">120</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8b0f78f3be042c62fb792803c864b2e2.png" alt="凌然" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">凌然</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">0.3</span>
                      <span class="kda2">0 / 3 / 1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5717</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">357</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15805</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">960.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">68.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">79977</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4515.1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">32.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">100%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:16:27</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking1">121</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/e85acf88871122e934de841cae2021e4.png" alt="可豪" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">可豪</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">0.8</span>
                      <span class="kda2">2 / 6 / 3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15300</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">765</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69835</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3345.4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">69%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">135219</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4490.9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">21.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:20:53</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking2">122</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/54deb50c5315d2e18ef58fbeaf1f1778.png" alt="Best" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">Best</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">2</span>
                      <span class="kda2">1 / 5 / 9</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">9</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">8074</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">403</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">13.1%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">30368</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1459</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">7.6%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">58.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">131263</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5888.8</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">71%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:20:49</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ranking3">123</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/5b4d1e1ddbb7294001b2120b5aa7662c.png" alt="小求" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">小求</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">0.8</span>
                      <span class="kda2">1 / 5 / 3</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6918</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">532</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">38549</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2900.3</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">18.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">100%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">48216</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3439.6</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">15.8%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">50%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:13:18</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">124</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/7cc6c9642247d873cdee6a140a3beebf.png" alt="话诗" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">话诗</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">0.7</span>
                      <span class="kda2">0 / 1.5 / 1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">5851.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">439.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">16.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55907.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4098.7</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">31.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">189.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">26927.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1857.2</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">10.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">66.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:13:50</div>
                  </td>
                </tr><tr class="c-table__row">
                  <td>
                    <div class="cell">
                      <span class="ranking ">125</span>
                    </div>
                  </td>
                  <td>
                    <div class="cell">
                      <div class="cell-img-name">
                        <div class="imgBox">
                          <img src="https://smobatv-pic.tga.qq.com/8f3b2498ca11603c682a4ce871587728.png" alt="傲神" onerror="javascript:this.src='//game.gtimg.cn/images/yxzj/m/matchdata/img/detail/user-icon.png';">
                        </div>
                        <span class="cell-name">傲神</span>
                      </div>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">
                      <span class="kda1">0.3</span>
                      <span class="kda2">0 / 4 / 1</span>
                    </div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">4</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">1</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">6248</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">624</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22.4%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">22290</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">2067</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">14.5%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">64.7%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">55877</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">3929.5</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">19.3%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">0%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">20%</div>
                  </td>
                  <td class="is-hidden">
                    <div class="cell">00:10:47</div>
                  </td>
                </tr></tbody>
            </table></div></div></div>
          </div>
        </div>
        <div class="null-dom dn">
          <div class="imgbox">
            <img src="//game.gtimg.cn/images/yxzj/matchdata/null.png" alt="暂无数据">
          </div>
          <span class="null-text"> 暂无数据</span>
        </div>
        <div class="moreBtns-wrap" style="">
          <div class="moreBtns">
            <a href="javascript:void(0);" class="btns">查看更多数据</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="linkage-wrap" id="linkage-wrap">
    <ul class="linkage-left clearfix" id="linkage-left">
      <li class="" position-id="6">
        <span class="sel-img"> </span>
        <span class="sel-name">对抗路</span>
        <span class="icon-t-right"></span>
      </li>
      <li class="" position-id="5">
        <span class="sel-img"> </span>
        <span class="sel-name">打野</span>
        <span class="icon-t-right"></span>
      </li>
      <li position-id="2">
        <span class="sel-img"> </span>
        <span class="sel-name">中路</span>
        <span class="icon-t-right"></span>
      </li>
      <li position-id="7">
        <span class="sel-img"> </span>
        <span class="sel-name">发育路</span>
        <span class="icon-t-right"></span>
      </li>
      <li position-id="4">
        <span class="sel-img"> </span>
        <span class="sel-name">游走</span>
        <span class="icon-t-right"></span>
      </li>
    </ul>
    <div class="linkage-right" id="linkage-right-box">
      <ul id="linkage-right-ul0"><li class="" openid="412F33F111FAA708495F3A97655CACB7">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/3c367d6e5ca7a2b79a685f05a1eb8589.png" alt="An">
          </div>
          <div class="cn-box">
            <span class="c-n">An</span>
            <span class="c-n1">西安WE</span>
          </div>
        </li><li class="" openid="978A761694D113E6353AC26C2B4CA160">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/8b0f78f3be042c62fb792803c864b2e2.png" alt="凌然">
          </div>
          <div class="cn-box">
            <span class="c-n">凌然</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="A19CF9FA3907681E92FA3E685122A32A">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/de4b9d54a1c9bfdffea83e29080e0aa9.png" alt="归期">
          </div>
          <div class="cn-box">
            <span class="c-n">归期</span>
            <span class="c-n1">重庆狼队</span>
          </div>
        </li><li class="" openid="2D37ECDC183F42AF0D57C2A646553640">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/0328bf8c0c2fc7e681a8a9604be62773.png" alt="景青">
          </div>
          <div class="cn-box">
            <span class="c-n">景青</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="122DBA5DD9DDE09374E7D0C002BADF25">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/b56f5210f974dc282e71b4ed4b79d16a.png" alt="梓轩">
          </div>
          <div class="cn-box">
            <span class="c-n">梓轩</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="A4F5BBC8EF3DE26F0DB66A63C1DCC954">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/8d45528e4577c5ecb17f2aa37a78dde4.png" alt="梓墨">
          </div>
          <div class="cn-box">
            <span class="c-n">梓墨</span>
            <span class="c-n1">北京WB</span>
          </div>
        </li><li class="" openid="23A681216737DCB3AFDF9EA80BA2634C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/34b847d9d4acf1fb377d2b4fd50af251.png" alt="誓约">
          </div>
          <div class="cn-box">
            <span class="c-n">誓约</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="75F1305CE134654648696BDFCD536C54">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/37f7d0359012b5e38e44202f686f271e.png" alt="百兽">
          </div>
          <div class="cn-box">
            <span class="c-n">百兽</span>
            <span class="c-n1">佛山DRG</span>
          </div>
        </li><li class="" openid="A727955E2BBCC4F98A02DC882A4E0A69">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/9b3cef40ec005b398e2e6c78d733eb70.png" alt="苏沫">
          </div>
          <div class="cn-box">
            <span class="c-n">苏沫</span>
            <span class="c-n1">长沙TES.A</span>
          </div>
        </li><li class="" openid="C3A82D04CDFB4A94E6C702FD2122DFB5">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/98e4fa9e72db8735209227f4f121b562.png" alt="东方">
          </div>
          <div class="cn-box">
            <span class="c-n">东方</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="E975CFD0CBA30C4AD52FC03F255E772F">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/28b0c1c86bba11d3777e41deef12d105.png" alt="啊泽">
          </div>
          <div class="cn-box">
            <span class="c-n">啊泽</span>
            <span class="c-n1">苏州KSG</span>
          </div>
        </li><li class="" openid="74DE2ED6351CD2D9F4C70B1B2823DECD">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/dfac89a287fb570f62dbc675d2efd526.png" alt="小七">
          </div>
          <div class="cn-box">
            <span class="c-n">小七</span>
            <span class="c-n1">上海RNG.M</span>
          </div>
        </li><li class="" openid="9F13A5F29B96662F5C16147FB67AB955">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/b01cb2ce26a07a06bc519a6ff847b59a.png" alt="星痕">
          </div>
          <div class="cn-box">
            <span class="c-n">星痕</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="9A3E415711EF5EB63681FC4048C8B3A7">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/7115f6074ac26e71cc3c750cdcd15ae0.png" alt="忆安">
          </div>
          <div class="cn-box">
            <span class="c-n">忆安</span>
            <span class="c-n1">成都AG超玩会</span>
          </div>
        </li><li class="" openid="5D548704F8DCD3CAA5318622481E0170">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/5def77d9d240b0e5fd44cdf3ed78f41d.png" alt="情川">
          </div>
          <div class="cn-box">
            <span class="c-n">情川</span>
            <span class="c-n1">深圳DYG</span>
          </div>
        </li><li class="" openid="3FC530E9096EE13683AA494C6D5F5828">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/4d6d01c683acf5694978910995f9a3eb.png" alt="背影">
          </div>
          <div class="cn-box">
            <span class="c-n">背影</span>
            <span class="c-n1">厦门VG</span>
          </div>
        </li><li class="" openid="A7AAD11E26643813D72EFEBD3B0EBD28">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/73a963d37fbc9af5d839d39b2075874b.png" alt="柠栀">
          </div>
          <div class="cn-box">
            <span class="c-n">柠栀</span>
            <span class="c-n1">上海EDG.M</span>
          </div>
        </li><li class="" openid="CAB50C107327AEF03FCFDD3988D32B83">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/d9c3b3c3ef3da4614fb778678ce840a2.png" alt="仙语">
          </div>
          <div class="cn-box">
            <span class="c-n">仙语</span>
            <span class="c-n1">西安WE</span>
          </div>
        </li><li class="" openid="98562D49FEF03808BFF786C0123E84AC">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/ade9f2ceee080e3d63dad74b30d252d6.png" alt="坦然（孙麟威）">
          </div>
          <div class="cn-box">
            <span class="c-n">坦然（孙麟威）</span>
            <span class="c-n1">武汉eStarPro</span>
          </div>
        </li><li class="" openid="DBFE99AEC8B415DF7F5B4B9700F1EC2D">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/8ae1b3437b077613bd309aa15bbee728.png" alt="酷偕">
          </div>
          <div class="cn-box">
            <span class="c-n">酷偕</span>
            <span class="c-n1">XYG</span>
          </div>
        </li><li class="" openid="AF0629B2EF727960E10AD14A52203250">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/8087dfbdf220f4dbf1c2d8ced3a5faed.png" alt="阿怪">
          </div>
          <div class="cn-box">
            <span class="c-n">阿怪</span>
            <span class="c-n1">郑州MTG</span>
          </div>
        </li><li class="" openid="2F9E170200A748CDDD6A8F5162908BCF">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/a9d72875be343eaa9ece04de5c15c04d.png" alt="小落">
          </div>
          <div class="cn-box">
            <span class="c-n">小落</span>
            <span class="c-n1">杭州LGD.NBW</span>
          </div>
        </li><li class="" openid="24A0AD15444D76177EC6A396CD143DAE">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/35faba2f440631c6314f9aae67c25f83.png" alt="杰杰">
          </div>
          <div class="cn-box">
            <span class="c-n">杰杰</span>
            <span class="c-n1">深圳DYG</span>
          </div>
        </li><li class="" openid="B092BD533E4E740EF69BA8BF6D78E0C0">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/d0f5e9f6fee630bf5519cae6d1da095a.png" alt="无上">
          </div>
          <div class="cn-box">
            <span class="c-n">无上</span>
            <span class="c-n1">厦门VG</span>
          </div>
        </li><li class="" openid="81AEA3A32BA205D61F400FA612808490">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/5cd022c1258f158b76b9856a9fb52389.png" alt="Fly">
          </div>
          <div class="cn-box">
            <span class="c-n">Fly</span>
            <span class="c-n1">重庆狼队</span>
          </div>
        </li><li class="" openid="7E1379DA0DE522674BE6D3D950792E19">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/42c878fddfd0d188f155b6c497e0c5c8.png" alt="清清">
          </div>
          <div class="cn-box">
            <span class="c-n">清清</span>
            <span class="c-n1">广州TTG</span>
          </div>
        </li><li class="" openid="AC399A1E51367A603883DBCCD6DB15A9">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/b3dcd48a50cc8b4fd2a3479614157382.png" alt="自渡">
          </div>
          <div class="cn-box">
            <span class="c-n">自渡</span>
            <span class="c-n1">西安WE</span>
          </div>
        </li></ul>
      <ul id="linkage-right-ul1"><li class="" openid="7882EEA70EFA4E02073D53B53587DF5D">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/7bcd79d0e0a980c3b116ed2b2a27b0d7.png" alt="林一">
          </div>
          <div class="cn-box">
            <span class="c-n">林一</span>
            <span class="c-n1">西安WE</span>
          </div>
        </li><li class="" openid="B61E31C87EB42BE852DEADE5273AB0DE">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/b762a5abeaa00cd1da6fdd77c490161b.png" alt="暖阳（林恒）">
          </div>
          <div class="cn-box">
            <span class="c-n">暖阳（林恒）</span>
            <span class="c-n1">北京WB</span>
          </div>
        </li><li class="" openid="4A0A09289775D2E149FAC04A94E8E706">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/5ce064c461a25bc1594d17a707e975a4.png" alt="今屿">
          </div>
          <div class="cn-box">
            <span class="c-n">今屿</span>
            <span class="c-n1">苏州KSG</span>
          </div>
        </li><li class="" openid="D218F9422931A172DFE2B9160C646C4B">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/9573fcc4b7d8805532f762ed6785edaa.png" alt="鹏鹏">
          </div>
          <div class="cn-box">
            <span class="c-n">鹏鹏</span>
            <span class="c-n1">佛山DRG</span>
          </div>
        </li><li class="" openid="C0BDDF50FB07FCE424537BFE33078807">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/ce86be8444a4587fd6a5201d2a1fb4ed.png" alt="不然">
          </div>
          <div class="cn-box">
            <span class="c-n">不然</span>
            <span class="c-n1">广州TTG</span>
          </div>
        </li><li class="" openid="83C9A146D58BCDA705A7E62DBB5DF896">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/4d3742c88bdd31560a43ff09ab5e2783.png" alt="冰然">
          </div>
          <div class="cn-box">
            <span class="c-n">冰然</span>
            <span class="c-n1">西安WE</span>
          </div>
        </li><li class="" openid="3D0C6EA77EAB209F792CABCCD28704BC">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/1e8f31a72ea4d38212bdbf473c55ee9e.png" alt="梓凡">
          </div>
          <div class="cn-box">
            <span class="c-n">梓凡</span>
            <span class="c-n1">西安WE</span>
          </div>
        </li><li class="" openid="7198CC5243D103B21A24B12773C886F1">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/e85acf88871122e934de841cae2021e4.png" alt="可豪">
          </div>
          <div class="cn-box">
            <span class="c-n">可豪</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="D6D4C5BC0F9EA17C73027A40EA70EA47">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/8ee4721ed5162f123e89bcc47a30d0e3.png" alt="Qy">
          </div>
          <div class="cn-box">
            <span class="c-n">Qy</span>
            <span class="c-n1">厦门VG</span>
          </div>
        </li><li class="" openid="449B838A53A50941F4ED1588CCBEDC5C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/04300319226899b16d9e7ade24d6e314.png" alt="以然">
          </div>
          <div class="cn-box">
            <span class="c-n">以然</span>
            <span class="c-n1">长沙TES.A</span>
          </div>
        </li><li class="" openid="2A5E5F2CCBC300E9EE7466A31B075EBB">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/9f4f7b1b8aefb81a33a98c843d4fc3cc.png" alt="九月">
          </div>
          <div class="cn-box">
            <span class="c-n">九月</span>
            <span class="c-n1">XYG</span>
          </div>
        </li><li class="" openid="FB8D160A5A68A07F5BD182DF76746138">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/0bc827584405baaceb878f98453ff248.png" alt="玄影">
          </div>
          <div class="cn-box">
            <span class="c-n">玄影</span>
            <span class="c-n1">上海EDG.M</span>
          </div>
        </li><li class="" openid="B958F82CC8496CA75AD036E61070570F">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/8bc3ee8cf44809ac7f6cf9f3db18bfbd.png" alt="赤辰">
          </div>
          <div class="cn-box">
            <span class="c-n">赤辰</span>
            <span class="c-n1">杭州LGD.NBW</span>
          </div>
        </li><li class="" openid="8C17F882648467792BCF6BDFD129D417">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/fbe28816578b5b5dcb758ce547ac5818.png" alt="晚星">
          </div>
          <div class="cn-box">
            <span class="c-n">晚星</span>
            <span class="c-n1">苏州KSG</span>
          </div>
        </li><li class="" openid="32A60408B2D697ABC6F8F84919412C37">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/a5f65ff7a7665af4718b90f48b76789c.png" alt="小胖">
          </div>
          <div class="cn-box">
            <span class="c-n">小胖</span>
            <span class="c-n1">重庆狼队</span>
          </div>
        </li><li class="" openid="F95EE73A43207678BF73129A2717E243">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/0588a8dd00258118b5cf1fcb610556af.png" alt="无畏">
          </div>
          <div class="cn-box">
            <span class="c-n">无畏</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="D3A29E426E009F260F9A0381884C2B4D">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/926ae6a4e63c48e1ec989ae0df604f0f.png" alt="顾兴">
          </div>
          <div class="cn-box">
            <span class="c-n">顾兴</span>
            <span class="c-n1">长沙TES.A</span>
          </div>
        </li><li class="" openid="7D1D29C1629432D8FA2E1CE299D1DF0C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/7711821e098a9853ce69bd6903b907cc.png" alt="小义">
          </div>
          <div class="cn-box">
            <span class="c-n">小义</span>
            <span class="c-n1">深圳DYG</span>
          </div>
        </li><li class="" openid="D33A2BE38DAB79944F465DF0CF191E87">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/0af445ace86a94640448d1b6cd810d05.png" alt="小椿">
          </div>
          <div class="cn-box">
            <span class="c-n">小椿</span>
            <span class="c-n1">成都AG超玩会</span>
          </div>
        </li><li class="" openid="6317ACA4810A9CE2501FA24B0050C02F">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/11872ff2e53bc3fc33d028cc9daf749d.png" alt="花海（罗思源）">
          </div>
          <div class="cn-box">
            <span class="c-n">花海（罗思源）</span>
            <span class="c-n1">武汉eStarPro</span>
          </div>
        </li><li class="" openid="814C5DD9BC3171DB8804746F9842B92F">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/395506052f0188bda91ff4934838cc93.png" alt="晚秋">
          </div>
          <div class="cn-box">
            <span class="c-n">晚秋</span>
            <span class="c-n1">上海RNG.M</span>
          </div>
        </li><li class="" openid="EFF304B568FA6EFAD8B77E4F8EC43C47">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/ab0ad160d0a21ab9186176d1b819da39.png" alt="季节">
          </div>
          <div class="cn-box">
            <span class="c-n">季节</span>
            <span class="c-n1">厦门VG</span>
          </div>
        </li><li class="" openid="866FEC62A79776028B5EF5D11A6631E1">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/e9a35c0f92bd12e7ca50af991b5b59a4.png" alt="迷途">
          </div>
          <div class="cn-box">
            <span class="c-n">迷途</span>
            <span class="c-n1">郑州MTG</span>
          </div>
        </li><li class="" openid="FEC77937DF7DD29C1BEAE6DE2456AFF3">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/e1906088d0ae9e9d2c0c2ae4933748fd.png" alt="未央">
          </div>
          <div class="cn-box">
            <span class="c-n">未央</span>
            <span class="c-n1">郑州MTG</span>
          </div>
        </li><li class="" openid="DDF81B4CDED41BEECC7CC974BE2B5DA9">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/a94ae4eeea3d9a98a5bf286c302e26f2.png" alt="小夜">
          </div>
          <div class="cn-box">
            <span class="c-n">小夜</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="FD264102E22DD2F879DB60FA07FF4A00">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/8f3b2498ca11603c682a4ce871587728.png" alt="傲神">
          </div>
          <div class="cn-box">
            <span class="c-n">傲神</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="B474B7B36B32E5F99E09D3ADC732F844">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/a2a8b6d77f5f3f921406de464abe3216.png" alt="钟意">
          </div>
          <div class="cn-box">
            <span class="c-n">钟意</span>
            <span class="c-n1">成都AG超玩会</span>
          </div>
        </li></ul>
      <ul id="linkage-right-ul2"><li class="" openid="C2A0F3FB93F7CD5613AE375B4B1D9C94">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/63c9ee50a54d077c0d7af79e59c0b7cc.png" alt="月色">
          </div>
          <div class="cn-box">
            <span class="c-n">月色</span>
            <span class="c-n1">重庆狼队</span>
          </div>
        </li><li class="" openid="9D9BA884970D4843EBCBA67AE45DFB47">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/3109a021ad37fbc536c5dc51405b8654.png" alt="向鱼">
          </div>
          <div class="cn-box">
            <span class="c-n">向鱼</span>
            <span class="c-n1">重庆狼队</span>
          </div>
        </li><li class="" openid="93BDAB623A187FD94E8CA51CCA1F1A6D">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/561864fc422e0fece270a52885fc8c74.png" alt="小羽">
          </div>
          <div class="cn-box">
            <span class="c-n">小羽</span>
            <span class="c-n1">上海RNG.M</span>
          </div>
        </li><li class="" openid="6E4660D69C6B7CD98021534EC5A6D0C5">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/37c2f3e3d084f4baca8f2533c806c3c4.png" alt="秋沫">
          </div>
          <div class="cn-box">
            <span class="c-n">秋沫</span>
            <span class="c-n1">喵鱼</span>
          </div>
        </li><li class="" openid="0AF35E9A9507940BE374612D954C23E1">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/cdd628c5a4e9fffa672d0df64fb110da.png" alt="灵梦">
          </div>
          <div class="cn-box">
            <span class="c-n">灵梦</span>
            <span class="c-n1">XYG</span>
          </div>
        </li><li class="" openid="AABAA95A653AF1F147A43A0627DBAEA6">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/84ebf5c426b75033b4e1df73fbe5cf2a.png" alt="决明">
          </div>
          <div class="cn-box">
            <span class="c-n">决明</span>
            <span class="c-n1">深圳DYG</span>
          </div>
        </li><li class="" openid="5E31B5644BB92B93CAE202FDBF8CCD5B">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/03d1c607fdee6e1f4526d9568ae165d8.png" alt="青枫">
          </div>
          <div class="cn-box">
            <span class="c-n">青枫</span>
            <span class="c-n1">佛山DRG</span>
          </div>
        </li><li class="" openid="FC5ABA0CFD7BAB3E6AD935FC94980E3E">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/beb7d3d855278db7fc92dbd7952432a8.png" alt="一曲">
          </div>
          <div class="cn-box">
            <span class="c-n">一曲</span>
            <span class="c-n1">苏州KSG</span>
          </div>
        </li><li class="" openid="3DB7CBEEB6F80096A052005A0F1762F2">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/54deb50c5315d2e18ef58fbeaf1f1778.png" alt="Best">
          </div>
          <div class="cn-box">
            <span class="c-n">Best</span>
            <span class="c-n1">成都AG超玩会</span>
          </div>
        </li><li class="" openid="E8256E30FDF534F373C3EE437A1E1C77">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/c9bd1afee0b367315b98a831f1389c99.png" alt="铃铛">
          </div>
          <div class="cn-box">
            <span class="c-n">铃铛</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="3B71649AB0EDA28C7B72C8FB31D37EBF">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/47e30493ec817b2c34cf5c82f5b58d9c.png" alt="幕色">
          </div>
          <div class="cn-box">
            <span class="c-n">幕色</span>
            <span class="c-n1">长沙TES.A</span>
          </div>
        </li><li class="" openid="F1B2BA5A27FE61518DCC510C73288D9C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/276858cb556f317c2b5ba8735800da28.png" alt="千世">
          </div>
          <div class="cn-box">
            <span class="c-n">千世</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="B9134A31BCF50E4600D1DEDFB79A2735">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/47426b6d08ba1b9eb5d9ae750dba2e1d.png" alt="清融">
          </div>
          <div class="cn-box">
            <span class="c-n">清融</span>
            <span class="c-n1">武汉eStarPro</span>
          </div>
        </li><li class="" openid="72E2A6C9A3D10B063D0AC5FE559213DA">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/14541912d6728e93c66a42a23bf32cfe.png" alt="花卷">
          </div>
          <div class="cn-box">
            <span class="c-n">花卷</span>
            <span class="c-n1">北京WB</span>
          </div>
        </li><li class="" openid="73D09DF6368EAA1198B9B43DCDCA8536">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/f9506254c198d2d0db3fff0527893892.png" alt="末将">
          </div>
          <div class="cn-box">
            <span class="c-n">末将</span>
            <span class="c-n1">厦门VG</span>
          </div>
        </li><li class="" openid="7C27EC6C772F1B8CCA48FDC7E73E9113">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/5b4d1e1ddbb7294001b2120b5aa7662c.png" alt="小求">
          </div>
          <div class="cn-box">
            <span class="c-n">小求</span>
            <span class="c-n1">上海RNG.M</span>
          </div>
        </li><li class="" openid="6818B8E83EBAF33F8468BF4347669EA5">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/d8f8ea8bf065993c5a039129c836e113.png" alt="长生">
          </div>
          <div class="cn-box">
            <span class="c-n">长生</span>
            <span class="c-n1">成都AG超玩会</span>
          </div>
        </li><li class="" openid="6646744A490CA02AFD82E4B0237160F9">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/7cc6c9642247d873cdee6a140a3beebf.png" alt="话诗">
          </div>
          <div class="cn-box">
            <span class="c-n">话诗</span>
            <span class="c-n1">杭州LGD.NBW</span>
          </div>
        </li><li class="" openid="BA000B75F8664BAD7DEE3DCB54CE552C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/5933ec732ac62f3a76813239d4217ae4.png" alt="早点">
          </div>
          <div class="cn-box">
            <span class="c-n">早点</span>
            <span class="c-n1">杭州LGD.NBW</span>
          </div>
        </li><li class="" openid="F7FB3A63ECC8E9402D7B13C04899B16E">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/268ab209ef89f2aa4bd81b452e9bac26.png" alt="文帝">
          </div>
          <div class="cn-box">
            <span class="c-n">文帝</span>
            <span class="c-n1">深圳DYG</span>
          </div>
        </li><li class="" openid="07919D7B0D434FEB8F82A77D125A0B83">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/48a2ded453710c49b80989954dea1922.png" alt="情缘">
          </div>
          <div class="cn-box">
            <span class="c-n">情缘</span>
            <span class="c-n1">郑州MTG</span>
          </div>
        </li><li class="" openid="D8FC7AD6484F38686489D0870B217B5E">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/fd5ccf7df062feca229a9d5f47fccd2d.png" alt="Ming">
          </div>
          <div class="cn-box">
            <span class="c-n">Ming</span>
            <span class="c-n1">上海EDG.M</span>
          </div>
        </li><li class="" openid="5CAC8191AF8F3503F7D7C9B3A3D5D171">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/6d899f90a771b5aef541a5c548363764.png" alt="九尾">
          </div>
          <div class="cn-box">
            <span class="c-n">九尾</span>
            <span class="c-n1">广州TTG</span>
          </div>
        </li><li class="" openid="816BFDAB75DEBA53F3CFB6178F2F92BE">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/d7d43bc95a455c4acdc95c1a498e7ef2.png" alt="晨风">
          </div>
          <div class="cn-box">
            <span class="c-n">晨风</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li></ul>
      <ul id="linkage-right-ul3"><li class="" openid="DB381E8080F8CAE73858ACDFB587AA0E">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/cca0e32562495551f243e1f92274e547.png" alt="小久">
          </div>
          <div class="cn-box">
            <span class="c-n">小久</span>
            <span class="c-n1">郑州MTG</span>
          </div>
        </li><li class="" openid="E1C85A6A65AA4D95E7307650BBF7AEFE">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/2ddaf7b8d271e9ed87a458ec48c946bc.png" alt="小年">
          </div>
          <div class="cn-box">
            <span class="c-n">小年</span>
            <span class="c-n1">厦门VG</span>
          </div>
        </li><li class="" openid="25A5FF77BB55049116D0BB64A7C98B4A">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/1dc617e6ee4edc26f834b370dd0fb879.png" alt="绝意">
          </div>
          <div class="cn-box">
            <span class="c-n">绝意</span>
            <span class="c-n1">杭州LGD.NBW</span>
          </div>
        </li><li class="" openid="924F7C93F262FC99443B7C27E9A3D6AA">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/0d8d108ab2c3a10240430bbecce51e2f.png" alt="一诺（徐必成）">
          </div>
          <div class="cn-box">
            <span class="c-n">一诺（徐必成）</span>
            <span class="c-n1">成都AG超玩会</span>
          </div>
        </li><li class="" openid="576982DDE588DFBF070EE568BC165EE7">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/12d0811490492112e295bd0409324003.png" alt="江城">
          </div>
          <div class="cn-box">
            <span class="c-n">江城</span>
            <span class="c-n1">北京WB</span>
          </div>
        </li><li class="" openid="5BD8345514032655E8EED144DDD5D6B3">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/3131a3a52761b06dcb89c5ab7f66e52e.png" alt="风劫">
          </div>
          <div class="cn-box">
            <span class="c-n">风劫</span>
            <span class="c-n1">武汉eStarPro</span>
          </div>
        </li><li class="" openid="647740157E919B82FBFCBFBB48392E0C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/d6d8526e6342b92e8d01233ccbd5df94.png" alt="Roc">
          </div>
          <div class="cn-box">
            <span class="c-n">Roc</span>
            <span class="c-n1">上海EDG.M</span>
          </div>
        </li><li class="" openid="6FE1A67E567B78EE8A9BC5863D5BB791">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/2a64c518a7e4aeff978597d3011b75f4.png" alt="冰冰">
          </div>
          <div class="cn-box">
            <span class="c-n">冰冰</span>
            <span class="c-n1">上海RNG.M</span>
          </div>
        </li><li class="" openid="E20DC214C3065406F4162B17E37030F4">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/7c19f73653eebeb163b7861ce9961e6a.png" alt="花云">
          </div>
          <div class="cn-box">
            <span class="c-n">花云</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="DDAB661D2D842BADB052FA61CA9E6139">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/38e591cf1ed8efa83ea56f34bbb88af7.png" alt="花月">
          </div>
          <div class="cn-box">
            <span class="c-n">花月</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="9924A7BAAFFAEF9B3CB37A8DD7E9A224">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/d650a1c4a421465ea1324f85691432cd.png" alt="傲寒">
          </div>
          <div class="cn-box">
            <span class="c-n">傲寒</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="F0F65882793C8CB1D58C085BCD522A77">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/fcdd4da0c20422cebc71a35df5a20bfb.png" alt="蓝桉">
          </div>
          <div class="cn-box">
            <span class="c-n">蓝桉</span>
            <span class="c-n1">长沙TES.A</span>
          </div>
        </li><li class="" openid="B85FF8B85DEC3E142B8FD38CF06AE36F">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/0cdf1dd856cab1fd5475977c82f9d658.png" alt="钎城">
          </div>
          <div class="cn-box">
            <span class="c-n">钎城</span>
            <span class="c-n1">深圳DYG</span>
          </div>
        </li><li class="" openid="A9A6C2449683B006DBF49334AE23E939">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/cd3b48b9f8fe8e96abab73573cd83965.png" alt="风箫">
          </div>
          <div class="cn-box">
            <span class="c-n">风箫</span>
            <span class="c-n1">广州TTG</span>
          </div>
        </li><li class="" openid="5E839CBBEC7B59598BFEAA3EB1D92696">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/e97d18a7b189150074b0bf345e748842.png" alt="小玖">
          </div>
          <div class="cn-box">
            <span class="c-n">小玖</span>
            <span class="c-n1">苏州KSG</span>
          </div>
        </li><li class="" openid="DDD0D18080016E5DD9E39DD738BC661C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/43b28d3e73ace965ee0bd5561258bace.png" alt="秀豆">
          </div>
          <div class="cn-box">
            <span class="c-n">秀豆</span>
            <span class="c-n1">XYG</span>
          </div>
        </li><li class="" openid="891E14BB89089AB10610A3566750F687">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/9e2b874427ddb2f23452748c340b266a.png" alt="梦岚">
          </div>
          <div class="cn-box">
            <span class="c-n">梦岚</span>
            <span class="c-n1">佛山DRG</span>
          </div>
        </li><li class="" openid="E2DA8DAFB90822DA6DA39C6FC40C4172">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/f50df692e9332268fc0461bc15dc09fb.png" alt="易峥">
          </div>
          <div class="cn-box">
            <span class="c-n">易峥</span>
            <span class="c-n1">武汉eStarPro</span>
          </div>
        </li><li class="" openid="E90749297F982867C6C4ABFE0692745C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/6476ebef7ce9703c7d6a9eef1973b92c.png" alt="佩恩">
          </div>
          <div class="cn-box">
            <span class="c-n">佩恩</span>
            <span class="c-n1">西安WE</span>
          </div>
        </li><li class="" openid="C9D941685D82271FE93B9D835B50BDBE">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/ca303f0f42b7ce8619dc433c3ed69b23.png" alt="妖刀">
          </div>
          <div class="cn-box">
            <span class="c-n">妖刀</span>
            <span class="c-n1">重庆狼队</span>
          </div>
        </li><li class="" openid="2D8E2E91721A5FB23C0A3F2542B02650">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/2109f8770f35fe7af93e8e2866bb393d.png" alt="乔兮">
          </div>
          <div class="cn-box">
            <span class="c-n">乔兮</span>
            <span class="c-n1">北京WB</span>
          </div>
        </li></ul>
      <ul id="linkage-right-ul4"><li class="" openid="B9E7045B1D667DD896F3A19BB8126880">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/831ad155e862a0da8c048c80ae873aaf.png" alt="小崽">
          </div>
          <div class="cn-box">
            <span class="c-n">小崽</span>
            <span class="c-n1">杭州LGD.NBW</span>
          </div>
        </li><li class="" openid="157F28BAFB849C28C003AFD615E0F7B0">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/573ca193e4c832d81953b2245713471e.png" alt="小磊">
          </div>
          <div class="cn-box">
            <span class="c-n">小磊</span>
            <span class="c-n1">厦门VG</span>
          </div>
        </li><li class="" openid="A25A35A18EE5DC93117789871D929E83">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/c887c33254a27e4b6990f4c52f33d9df.png" alt="Cat">
          </div>
          <div class="cn-box">
            <span class="c-n">Cat</span>
            <span class="c-n1">成都AG超玩会</span>
          </div>
        </li><li class="" openid="E8A2A312B6A17CDAA74FF27EBEE1E75A">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/92b982171748e8d0e08e29d817e4d164.png" alt="不弃">
          </div>
          <div class="cn-box">
            <span class="c-n">不弃</span>
            <span class="c-n1">深圳DYG</span>
          </div>
        </li><li class="" openid="51C3A4979ADDE9E23CE73E176DE64319">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/988d4be506b65f5de79bd2598d2baa2c.png" alt="爱思">
          </div>
          <div class="cn-box">
            <span class="c-n">爱思</span>
            <span class="c-n1">上海EDG.M</span>
          </div>
        </li><li class="" openid="2AE8DD8F971354AEE07F078881E87AE9">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/47767bd2507a965cf4c38eabb91b8e9a.png" alt="久凡">
          </div>
          <div class="cn-box">
            <span class="c-n">久凡</span>
            <span class="c-n1">郑州MTG</span>
          </div>
        </li><li class="" openid="FD70952C1A9B936EDDB00609A7440670">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/fb08390611f294a193e26c089a9e9b46.png" alt="十三">
          </div>
          <div class="cn-box">
            <span class="c-n">十三</span>
            <span class="c-n1">厦门VG</span>
          </div>
        </li><li class="" openid="1D9FE3C27E1D59E8DAC386A9962F0955">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/faac4faa28d92bddc3e143afdd057921.png" alt="阿改">
          </div>
          <div class="cn-box">
            <span class="c-n">阿改</span>
            <span class="c-n1">佛山DRG</span>
          </div>
        </li><li class="" openid="B60BEC66456FDE26DDF9B6F7BCCE6131">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/f019291412bf15426a5cbc39afd18591.png" alt="冰尘">
          </div>
          <div class="cn-box">
            <span class="c-n">冰尘</span>
            <span class="c-n1">长沙TES.A</span>
          </div>
        </li><li class="" openid="A3CC4165FF162CA5177FF2B2A38C27C0">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/36ee63cce8a0061c6c2d887f2ebbe622.png" alt="一笙">
          </div>
          <div class="cn-box">
            <span class="c-n">一笙</span>
            <span class="c-n1">重庆狼队</span>
          </div>
        </li><li class="" openid="8B242820C3F35C0DEFB9F257D4020BC4">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/6031efec47f5ad279253f962635a0ecc.png" alt="星宇">
          </div>
          <div class="cn-box">
            <span class="c-n">星宇</span>
            <span class="c-n1">北京WB</span>
          </div>
        </li><li class="" openid="173D32D798D7CA169EB60BE1B0D4E4FB">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/2ee59d91feade6c3b6e42e74d289ec44.png" alt="久酷">
          </div>
          <div class="cn-box">
            <span class="c-n">久酷</span>
            <span class="c-n1">南京Hero久竞</span>
          </div>
        </li><li class="" openid="6D54271544D17B374436D7189EEBC522">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/eb48fec336a3035bbaff57bda95d65c5.png" alt="阿豆（蒋涛）">
          </div>
          <div class="cn-box">
            <span class="c-n">阿豆（蒋涛）</span>
            <span class="c-n1">广州TTG</span>
          </div>
        </li><li class="" openid="A62056113852C8BD1AE1171C33D32ABA">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/2a4ea3d4cca408009c033f13509ed748.png" alt="一门">
          </div>
          <div class="cn-box">
            <span class="c-n">一门</span>
            <span class="c-n1">XYG</span>
          </div>
        </li><li class="" openid="6A3F17E8187CCCAB514B6BE9A8F7C209">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/fabf19fb0188947220f55e0a309fe101.png" alt="子阳">
          </div>
          <div class="cn-box">
            <span class="c-n">子阳</span>
            <span class="c-n1">武汉eStarPro</span>
          </div>
        </li><li class="" openid="68CC4C3EBFAE38D69ED5443B9958DA85">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/a21c30d04be583356cb6e8cffb89529e.png" alt="稚念">
          </div>
          <div class="cn-box">
            <span class="c-n">稚念</span>
            <span class="c-n1">深圳DYG</span>
          </div>
        </li><li class="" openid="F15B75401D3045CF1AB81B47BF68D43A">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/a53645eda564019b8c18572522170a01.png" alt="小A">
          </div>
          <div class="cn-box">
            <span class="c-n">小A</span>
            <span class="c-n1">苏州KSG</span>
          </div>
        </li><li class="" openid="F87C373893FEE91FC263955B00CA3D0B">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/9087aab872e1deb4f2346058b31d35cc.png" alt="雨雨">
          </div>
          <div class="cn-box">
            <span class="c-n">雨雨</span>
            <span class="c-n1">上海RNG.M</span>
          </div>
        </li><li class="" openid="AD5024CF823765963E8F42BDA2EA51DE">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/dee0b1d9815975dc77abc3f6beee2cf6.png" alt="夏竹">
          </div>
          <div class="cn-box">
            <span class="c-n">夏竹</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="558B8536033B16FEC1FF02F3E02FC1D1">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/c6c83917fb46d8108f687c23fb495959.png" alt="Zero">
          </div>
          <div class="cn-box">
            <span class="c-n">Zero</span>
            <span class="c-n1">上海RNG.M</span>
          </div>
        </li><li class="" openid="BB176EBA5A040011260420E47F5D8D6C">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/c5f03a87d36aef19a400d1d09365a35a.png" alt="无铭">
          </div>
          <div class="cn-box">
            <span class="c-n">无铭</span>
            <span class="c-n1">武汉eStarPro</span>
          </div>
        </li><li class="" openid="E4F91381CD2B14F963C84113B7E06665">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/ccdc5c98a1f46ba521ccafd69424f310.png" alt="羲和">
          </div>
          <div class="cn-box">
            <span class="c-n">羲和</span>
            <span class="c-n1">XYG</span>
          </div>
        </li><li class="" openid="25529FFCDDC56F87EF590AE5A502A142">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/eca2317db974f302eeeadb7718d4002c.png" alt="556">
          </div>
          <div class="cn-box">
            <span class="c-n">556</span>
            <span class="c-n1">西安WE</span>
          </div>
        </li><li class="" openid="6D24B00C1B9E76BCA81D5D7A01DEA2FB">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/98b7d418ea608c3f940042b2c9318285.png" alt="笑影">
          </div>
          <div class="cn-box">
            <span class="c-n">笑影</span>
            <span class="c-n1">济南RW侠</span>
          </div>
        </li><li class="" openid="29F240524C1D1CD365DEF6C5FB3163D0">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/60d74420e4df0e080b29c307368dacc6.png" alt="帆帆">
          </div>
          <div class="cn-box">
            <span class="c-n">帆帆</span>
            <span class="c-n1">广州TTG</span>
          </div>
        </li><li class="" openid="3E716DCD3F100C13FAC1F62A7C588D82">
          <span class="s-img"> </span>
          <div class="userimg">
            <img src="https://smobatv-pic.tga.qq.com/f6bfc9197e6dc0dfe8ffcac26544c8b8.png" alt="言梦">
          </div>
          <div class="cn-box">
            <span class="c-n">言梦</span>
            <span class="c-n1">上海EDG.M</span>
          </div>
        </li></ul>
    </div>

    <div class="ld-btns-box">
      <span class="ld-btn ld-btn-reset" id="ld-btn-reset">重置</span>
      <span class="ld-btn ld-btn-submit" id="ld-btn-submit">确定（<i>全部队员</i>）</span>
      <span class="ld-btn ld-btn-cancel" id="ld-btn-cancel">取消</span>
    </div>
  </div>

  <script src="js/lib/jquery-1.9.1.min.js"></script>
  <script src="js/lib/jquery.qrcode.min.js"></script>
  <!-- 必要插件：固定列滚动需要用到，鼠标滚动兼容多浏览器 -->
  <script src="js/lib/jqTable/js/jquery.mousewheel.min.js"></script>
  <!-- 总引入  -->
  <script src="js/lib/jqTable/js/zipJs/jqTable.all.min.js"></script>
  <script src="//pvp.qq.com/m/matchdata/js/json3.min.js"></script>
  <script src="//pvp.qq.com/m/matchdata/js/axios.min.js"></script>
  <script src="//pvp.qq.com/m/matchdata/js/public.js"></script>
  <script src="//pvp.qq.com/m/matchdata/js/league.js"></script>
  <script src="js/common.js"></script>  <div class="login-pop" id="login-pop">
  <div class="login-pop-bg"></div>
  <div class="login-content"> 
    <div class="closeIcon" onclick="closeloginsPop()"></div>
    <div class="title-pic">
      <img src="https://game.gtimg.cn/images/yxzj/matchdata/login1.png" alt="">
    </div>
    <p class="tips">请选择您登陆的平台</p>
    <div class="btns-wrap">
      <a href="javascript:void(0)" class="btns wechat"> <!-- onclick="showLoginPop('#wechat-pop')"-->
        <span>微信用户登录</span>
      </a>
      <a href="javascript:void(0)" class="btns qq"> <!-- onclick="showLoginPop('#qq-pop')" -->
        <span>QQ用户登录</span>
      </a>
    </div>
  </div>
</div>
<div class="login-pop" id="wechat-pop">
  <div class="login-pop-bg"></div>
  <div class="login-content wechat-content"> 
    <div class="closeIcon" onclick="closeloginsPop()"></div>
    <div class="wechat-titile">
      微信登录
    </div>
    <div class="wechat-img">
      <img src="https://game.gtimg.cn/images/yxzj/matchdata/qr.png" alt="微信登录二维码">
    </div>
    
   <p class="wechat-p">
    使用微信扫一扫登录
    “王者荣耀”
   </p>
  </div>
</div>
<div class="login-pop" id="qq-pop">
  <div class="login-pop-bg"></div>
  <div class="login-content qq-content"> 
    <div class="closeIcon" onclick="closeloginsPop()"></div>
    <div class="qq-titile">
      快速安全登录
    </div>
    <div class="qq-titile1">
     请使用<i class="i">QQ手机版</i>扫描二维码，
      或点击头像授权登录。
    </div>
    <div class="qq-img">
      <img src="https://game.gtimg.cn/images/yxzj/matchdata/qr.png" alt="微信登录二维码">
    </div>
    
   <p class="wechat-p-a">
    <a href="javascript:void(0)">账号密码登录</a>
    <i></i>
    <a href="javascript:void(0)">注册新账号 </a>
    <i></i>
    <a href="javascript:void(0)">意见反馈</a>
   </p>
  </div>
</div>
  <script src="js/playerDataConf.js"></script>
  <script src="js/playerData.js"></script>
  <script>
    function findRightLiSelect() {
      var len = $(".linkage-right").find("li.active").length;
      var text = "全部队员";
      text = len > 0 ? len + "名队员" : text;
      $("#ld-btn-submit i").html(text);
    }
    $(function () {
     
      //设置按钮文字
      $(".competition-list").on("click","li",function () { 
       
        $(this).toggleClass("active").siblings().removeClass("active")
       })
      //筛选
      // $("#table-header").on("click", ".h-item-p", function () {
      //   if ($(this).hasClass("activeup")) {
      //     $(this).removeClass("activeup");
      //   } else if ($(this).hasClass("activedown")) {
      //     $(this).addClass("activeup").removeClass("activedown");
      //   } else if (
      //     !$(this).hasClass("activedown") &&
      //     !$(this).hasClass("activeup")
      //   ) {
      //     $(this)
      //       .addClass("activedown")
      //       .parents("th")
      //       .siblings()
      //       .find(".h-item-p")
      //       .removeClass("activedown activeup");
      //   }
      // });

      //联动
      // $("#linkage-left").on("click", "li", function () {
      //   var index = $(this).index();
      //   $(this).addClass("cur").siblings().removeClass("cur");
      //   $("#linkage-right-ul" + index)
      //     .show()
      //     .siblings()
      //     .hide();
      // });
      // $("#ld-btn-cancel").on("click", function () {
      //   $("#linkage-wrap").hide();
      // });
      // $("#ld-btn-reset").on("click", function () {
      //   $(".linkage-left li").removeClass("activeAll activePart");
      //   $(".linkage-right li").removeClass("active");
      // });
      // $("#ld-btn-submit").on("click", function () {
      //   $("#linkage-wrap").hide();
      //   $(".pop-team").addClass("active");
      //   $(".pop-team img").attr("src","//game.gtimg.cn/images/yxzj/matchdata/sx-on.png")
      // });
      // $("#linkage-left").on("click", ".sel-img", function () {
      //   var parents = $(this).parents("li");
      //   var index = parents.index();
      //   if (!parents.hasClass("activeAll")) {
      //     parents.addClass("activeAll cur").siblings().removeClass("cur");
      //     $("#linkage-right-ul" + index)
      //       .show()
      //       .siblings()
      //       .hide();
      //     $("#linkage-right-ul" + index)
      //       .find("li")
      //       .addClass("active");
      //   } else {
      //     parents.removeClass("activeAll activePart");
      //     $("#linkage-right-ul" + index)
      //       .show()
      //       .find("li")
      //       .removeClass("active");
      //     $("#linkage-right-ul" + index)
      //       .siblings()
      //       .hide();
      //   }
      //   findRightLiSelect();
      //   return false;
      // });
      // $("#linkage-right-box").on("click", "li", function () {
      //   $(this).toggleClass("active");
      //   var parents = $(this).parent("ul");
      //   var index = parents.index();
      //   let activeLi = parents.find("li.active").length;
      //   let liLen = parents.find("li").length;
      //   if (liLen === activeLi) {
      //     $("#linkage-left li")
      //       .eq(index)
      //       .addClass("activeAll")
      //       .removeClass("activePart");
      //   } else {
      //     if (activeLi == 0) {
      //       $("#linkage-left li").eq(index).removeClass("activePart");
      //     } else {
      //       $("#linkage-left li")
      //         .eq(index)
      //         .addClass("activePart")
      //         .removeClass("activeAll");
      //     }
      //   }
      //   findRightLiSelect();
      // });
    });
  </script>
  <script src="//ossweb-img.qq.com/images/js/PTT/ping_tcss_tgideas_https_min.js"></script>
  <script type="text/javascript" src="//ossweb-img.qq.com/images/js/eas/eas.js" charset="utf-8" timeout="5000"></script><script type="text/javascript" src="//game.gtimg.cn/images/js/tdm/tdm.js" charset="utf-8" timeout="5000"></script><script type="text/javascript" src="//beacon.cdn.qq.com/sdk/4.5.7/beacon_web.min.js" charset="utf-8" timeout="5000"></script><script type="text/javascript" src="//game.gtimg.cn/images/js/xom/xom-2022031810.js" charset="utf-8" beacon-enable="" beacon-appkey="0WEB01DBSP4NCDKM" tcss-enable="" eas-enable="" tdm-enable=""></script>
  <script>
    var setSite={
      siteType:"os",
      pageType:"playerData",
      pageName:"选手结算数据榜单页",
      project:"match",
      osact:'0'
    };
    if(typeof(pgvMain)=='function')pgvMain();
  </script>


</body></html># 将你的HTML源代码粘贴在这里
"""

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html, 'html.parser')

# 找到包含表格数据的父级元素
table_parent = soup.find('div', {'class': 'c-table--main'})

# 找到表头和表体
table_header = table_parent.find('thead')
table_body = table_parent.find('tbody')

# 提取表头数据
headers = [header.text.strip() for header in table_header.find_all('div', {'class': 'h-item-p'})]

# 提取表格数据
data_rows = table_body.find_all('tr', {'class': 'c-table__row'})
table_data = []

for row in data_rows:
    row_data = [cell.text.strip() for cell in row.find_all('div', {'class': 'cell'})]
    table_data.append(row_data)

# 将表头和表格数据写入CSV文件
csv_file_path = 'table_data.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # 写入表头
    csv_writer.writerow(headers)
    
    # 写入表格数据
    csv_writer.writerows(table_data)

print(f'Data has been written to {csv_file_path}')