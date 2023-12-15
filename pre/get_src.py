from bs4 import BeautifulSoup
import csv

def extract_img_info(input_html):
    soup = BeautifulSoup(input_html, 'html.parser')

    # 找到所有img标签
    img_tags = soup.find_all('img')

    # 提取每个img标签的src和alt属性
    img_info_list = []
    for img_tag in img_tags:
        src = img_tag.get('src', '')
        alt = img_tag.get('alt', '')
        img_info_list.append({'src': src, 'alt': alt})

    return img_info_list

def save_to_csv(img_info_list, csv_filename='output.csv'):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['src', 'alt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 写入CSV文件头
        writer.writeheader()

        # 写入每行数据
        for img_info in img_info_list:
            writer.writerow(img_info)

# 示例HTML
html_content = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Page Title</title>
    <link rel="stylesheet" href="reset.css">
    <link rel="stylesheet" href="table.css">
    <link rel="stylesheet" href="team.css">
</head>

<body>

    <div class="linkage-wrap" id="linkage-wrap" style="display: block; left: 501px; top: 115px;">
        <ul class="linkage-left clearfix" id="linkage-left">
          <li class="cur" position-id="6">
            <span class="sel-img"> </span>
            <span class="sel-name">对抗路</span>
            <span class="icon-t-right"></span>
          </li>
          <li class="" position-id="5">
            <span class="sel-img"> </span>
            <span class="sel-name">打野</span>
            <span class="icon-t-right"></span>
          </li>
          <li position-id="2" class="">
            <span class="sel-img"> </span>
            <span class="sel-name">中路</span>
            <span class="icon-t-right"></span>
          </li>
          <li position-id="7" class="">
            <span class="sel-img"> </span>
            <span class="sel-name">发育路</span>
            <span class="icon-t-right"></span>
          </li>
          <li position-id="4" class="">
            <span class="sel-img"> </span>
            <span class="sel-name">游走</span>
            <span class="icon-t-right"></span>
          </li>
        </ul>
        <div class="linkage-right" id="linkage-right-box">
          <ul id="linkage-right-ul0" style="display: block;"><li class="" openid="7E1379DA0DE522674BE6D3D950792E19">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/42c878fddfd0d188f155b6c497e0c5c8.png" alt="清清">
              </div>
              <div class="cn-box">
                <span class="c-n">清清</span>
                <span class="c-n1">广州TTG</span>
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
            </li><li class="" openid="A19CF9FA3907681E92FA3E685122A32A">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/de4b9d54a1c9bfdffea83e29080e0aa9.png" alt="归期">
              </div>
              <div class="cn-box">
                <span class="c-n">归期</span>
                <span class="c-n1">重庆狼队</span>
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
            </li><li class="" openid="75F1305CE134654648696BDFCD536C54">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/37f7d0359012b5e38e44202f686f271e.png" alt="百兽">
              </div>
              <div class="cn-box">
                <span class="c-n">百兽</span>
                <span class="c-n1">佛山DRG</span>
              </div>
            </li><li class="" openid="412F33F111FAA708495F3A97655CACB7">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/3c367d6e5ca7a2b79a685f05a1eb8589.png" alt="An">
              </div>
              <div class="cn-box">
                <span class="c-n">An</span>
                <span class="c-n1">西安WE</span>
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
            </li><li class="" openid="122DBA5DD9DDE09374E7D0C002BADF25">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/b56f5210f974dc282e71b4ed4b79d16a.png" alt="梓轩">
              </div>
              <div class="cn-box">
                <span class="c-n">梓轩</span>
                <span class="c-n1">济南RW侠</span>
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
            </li><li class="" openid="A727955E2BBCC4F98A02DC882A4E0A69">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/9b3cef40ec005b398e2e6c78d733eb70.png" alt="苏沫">
              </div>
              <div class="cn-box">
                <span class="c-n">苏沫</span>
                <span class="c-n1">长沙TES.A</span>
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
            </li><li class="" openid="5D548704F8DCD3CAA5318622481E0170">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/5def77d9d240b0e5fd44cdf3ed78f41d.png" alt="情川">
              </div>
              <div class="cn-box">
                <span class="c-n">情川</span>
                <span class="c-n1">深圳DYG</span>
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
            </li><li class="" openid="AF0629B2EF727960E10AD14A52203250">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/8087dfbdf220f4dbf1c2d8ced3a5faed.png" alt="阿怪">
              </div>
              <div class="cn-box">
                <span class="c-n">阿怪</span>
                <span class="c-n1">郑州MTG</span>
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
            </li><li class="" openid="A7AAD11E26643813D72EFEBD3B0EBD28">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/73a963d37fbc9af5d839d39b2075874b.png" alt="柠栀">
              </div>
              <div class="cn-box">
                <span class="c-n">柠栀</span>
                <span class="c-n1">上海EDG.M</span>
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
            </li><li class="" openid="23A681216737DCB3AFDF9EA80BA2634C">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/34b847d9d4acf1fb377d2b4fd50af251.png" alt="誓约">
              </div>
              <div class="cn-box">
                <span class="c-n">誓约</span>
                <span class="c-n1">南京Hero久竞</span>
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
            </li><li class="" openid="2D37ECDC183F42AF0D57C2A646553640">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/0328bf8c0c2fc7e681a8a9604be62773.png" alt="景青">
              </div>
              <div class="cn-box">
                <span class="c-n">景青</span>
                <span class="c-n1">济南RW侠</span>
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
            </li><li class="" openid="2F9E170200A748CDDD6A8F5162908BCF">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/a9d72875be343eaa9ece04de5c15c04d.png" alt="小落">
              </div>
              <div class="cn-box">
                <span class="c-n">小落</span>
                <span class="c-n1">杭州LGD.NBW</span>
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
            </li><li class="" openid="CAB50C107327AEF03FCFDD3988D32B83">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/d9c3b3c3ef3da4614fb778678ce840a2.png" alt="仙语">
              </div>
              <div class="cn-box">
                <span class="c-n">仙语</span>
                <span class="c-n1">西安WE</span>
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
            </li><li class="" openid="DBFE99AEC8B415DF7F5B4B9700F1EC2D">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/8ae1b3437b077613bd309aa15bbee728.png" alt="酷偕">
              </div>
              <div class="cn-box">
                <span class="c-n">酷偕</span>
                <span class="c-n1">XYG</span>
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
            </li></ul>
          <ul id="linkage-right-ul1" style="display: none;"><li class="" openid="4A0A09289775D2E149FAC04A94E8E706">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/5ce064c461a25bc1594d17a707e975a4.png" alt="今屿">
              </div>
              <div class="cn-box">
                <span class="c-n">今屿</span>
                <span class="c-n1">苏州KSG</span>
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
            </li><li class="" openid="D6D4C5BC0F9EA17C73027A40EA70EA47">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/8ee4721ed5162f123e89bcc47a30d0e3.png" alt="Qy">
              </div>
              <div class="cn-box">
                <span class="c-n">Qy</span>
                <span class="c-n1">厦门VG</span>
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
            </li><li class="" openid="7198CC5243D103B21A24B12773C886F1">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/e85acf88871122e934de841cae2021e4.png" alt="可豪">
              </div>
              <div class="cn-box">
                <span class="c-n">可豪</span>
                <span class="c-n1">南京Hero久竞</span>
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
            </li><li class="" openid="EFF304B568FA6EFAD8B77E4F8EC43C47">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/ab0ad160d0a21ab9186176d1b819da39.png" alt="季节">
              </div>
              <div class="cn-box">
                <span class="c-n">季节</span>
                <span class="c-n1">厦门VG</span>
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
            </li><li class="" openid="F95EE73A43207678BF73129A2717E243">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/0588a8dd00258118b5cf1fcb610556af.png" alt="无畏">
              </div>
              <div class="cn-box">
                <span class="c-n">无畏</span>
                <span class="c-n1">南京Hero久竞</span>
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
            </li><li class="" openid="C0BDDF50FB07FCE424537BFE33078807">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/ce86be8444a4587fd6a5201d2a1fb4ed.png" alt="不然">
              </div>
              <div class="cn-box">
                <span class="c-n">不然</span>
                <span class="c-n1">广州TTG</span>
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
            </li><li class="" openid="83C9A146D58BCDA705A7E62DBB5DF896">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/4d3742c88bdd31560a43ff09ab5e2783.png" alt="冰然">
              </div>
              <div class="cn-box">
                <span class="c-n">冰然</span>
                <span class="c-n1">西安WE</span>
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
            </li><li class="" openid="814C5DD9BC3171DB8804746F9842B92F">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/395506052f0188bda91ff4934838cc93.png" alt="晚秋">
              </div>
              <div class="cn-box">
                <span class="c-n">晚秋</span>
                <span class="c-n1">上海RNG.M</span>
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
            </li><li class="" openid="449B838A53A50941F4ED1588CCBEDC5C">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/04300319226899b16d9e7ade24d6e314.png" alt="以然">
              </div>
              <div class="cn-box">
                <span class="c-n">以然</span>
                <span class="c-n1">长沙TES.A</span>
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
            </li><li class="" openid="3D0C6EA77EAB209F792CABCCD28704BC">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/1e8f31a72ea4d38212bdbf473c55ee9e.png" alt="梓凡">
              </div>
              <div class="cn-box">
                <span class="c-n">梓凡</span>
                <span class="c-n1">西安WE</span>
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
            </li><li class="" openid="FB8D160A5A68A07F5BD182DF76746138">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/0bc827584405baaceb878f98453ff248.png" alt="玄影">
              </div>
              <div class="cn-box">
                <span class="c-n">玄影</span>
                <span class="c-n1">上海EDG.M</span>
              </div>
            </li><li class="" openid="7882EEA70EFA4E02073D53B53587DF5D">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/7bcd79d0e0a980c3b116ed2b2a27b0d7.png" alt="林一">
              </div>
              <div class="cn-box">
                <span class="c-n">林一</span>
                <span class="c-n1">西安WE</span>
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
            </li><li class="" openid="B61E31C87EB42BE852DEADE5273AB0DE">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/b762a5abeaa00cd1da6fdd77c490161b.png" alt="暖阳（林恒）">
              </div>
              <div class="cn-box">
                <span class="c-n">暖阳（林恒）</span>
                <span class="c-n1">北京WB</span>
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
            </li></ul>
          <ul id="linkage-right-ul2" style="display: none;"><li class="" openid="B9134A31BCF50E4600D1DEDFB79A2735">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/47426b6d08ba1b9eb5d9ae750dba2e1d.png" alt="清融">
              </div>
              <div class="cn-box">
                <span class="c-n">清融</span>
                <span class="c-n1">武汉eStarPro</span>
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
            </li><li class="" openid="FC5ABA0CFD7BAB3E6AD935FC94980E3E">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/beb7d3d855278db7fc92dbd7952432a8.png" alt="一曲">
              </div>
              <div class="cn-box">
                <span class="c-n">一曲</span>
                <span class="c-n1">苏州KSG</span>
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
            </li><li class="" openid="93BDAB623A187FD94E8CA51CCA1F1A6D">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/561864fc422e0fece270a52885fc8c74.png" alt="小羽">
              </div>
              <div class="cn-box">
                <span class="c-n">小羽</span>
                <span class="c-n1">上海RNG.M</span>
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
            </li><li class="" openid="AABAA95A653AF1F147A43A0627DBAEA6">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/84ebf5c426b75033b4e1df73fbe5cf2a.png" alt="决明">
              </div>
              <div class="cn-box">
                <span class="c-n">决明</span>
                <span class="c-n1">深圳DYG</span>
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
            </li><li class="" openid="816BFDAB75DEBA53F3CFB6178F2F92BE">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/d7d43bc95a455c4acdc95c1a498e7ef2.png" alt="晨风">
              </div>
              <div class="cn-box">
                <span class="c-n">晨风</span>
                <span class="c-n1">济南RW侠</span>
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
            </li><li class="" openid="7C27EC6C772F1B8CCA48FDC7E73E9113">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/5b4d1e1ddbb7294001b2120b5aa7662c.png" alt="小求">
              </div>
              <div class="cn-box">
                <span class="c-n">小求</span>
                <span class="c-n1">上海RNG.M</span>
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
            </li><li class="" openid="C2A0F3FB93F7CD5613AE375B4B1D9C94">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/63c9ee50a54d077c0d7af79e59c0b7cc.png" alt="月色">
              </div>
              <div class="cn-box">
                <span class="c-n">月色</span>
                <span class="c-n1">重庆狼队</span>
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
            </li><li class="" openid="0AF35E9A9507940BE374612D954C23E1">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/cdd628c5a4e9fffa672d0df64fb110da.png" alt="灵梦">
              </div>
              <div class="cn-box">
                <span class="c-n">灵梦</span>
                <span class="c-n1">XYG</span>
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
            </li><li class="" openid="5CAC8191AF8F3503F7D7C9B3A3D5D171">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/6d899f90a771b5aef541a5c548363764.png" alt="九尾">
              </div>
              <div class="cn-box">
                <span class="c-n">九尾</span>
                <span class="c-n1">广州TTG</span>
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
            </li><li class="" openid="07919D7B0D434FEB8F82A77D125A0B83">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/48a2ded453710c49b80989954dea1922.png" alt="情缘">
              </div>
              <div class="cn-box">
                <span class="c-n">情缘</span>
                <span class="c-n1">郑州MTG</span>
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
            </li><li class="" openid="5E31B5644BB92B93CAE202FDBF8CCD5B">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/03d1c607fdee6e1f4526d9568ae165d8.png" alt="青枫">
              </div>
              <div class="cn-box">
                <span class="c-n">青枫</span>
                <span class="c-n1">佛山DRG</span>
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
            </li><li class="" openid="6818B8E83EBAF33F8468BF4347669EA5">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/d8f8ea8bf065993c5a039129c836e113.png" alt="长生">
              </div>
              <div class="cn-box">
                <span class="c-n">长生</span>
                <span class="c-n1">成都AG超玩会</span>
              </div>
            </li></ul>
          <ul id="linkage-right-ul3" style="display: none;"><li class="" openid="924F7C93F262FC99443B7C27E9A3D6AA">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/0d8d108ab2c3a10240430bbecce51e2f.png" alt="一诺（徐必成）">
              </div>
              <div class="cn-box">
                <span class="c-n">一诺（徐必成）</span>
                <span class="c-n1">成都AG超玩会</span>
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
            </li><li class="" openid="25A5FF77BB55049116D0BB64A7C98B4A">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/1dc617e6ee4edc26f834b370dd0fb879.png" alt="绝意">
              </div>
              <div class="cn-box">
                <span class="c-n">绝意</span>
                <span class="c-n1">杭州LGD.NBW</span>
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
            </li><li class="" openid="DDD0D18080016E5DD9E39DD738BC661C">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/43b28d3e73ace965ee0bd5561258bace.png" alt="秀豆">
              </div>
              <div class="cn-box">
                <span class="c-n">秀豆</span>
                <span class="c-n1">XYG</span>
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
            </li><li class="" openid="B85FF8B85DEC3E142B8FD38CF06AE36F">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/0cdf1dd856cab1fd5475977c82f9d658.png" alt="钎城">
              </div>
              <div class="cn-box">
                <span class="c-n">钎城</span>
                <span class="c-n1">深圳DYG</span>
              </div>
            </li><li class="" openid="DB381E8080F8CAE73858ACDFB587AA0E">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/cca0e32562495551f243e1f92274e547.png" alt="小久">
              </div>
              <div class="cn-box">
                <span class="c-n">小久</span>
                <span class="c-n1">郑州MTG</span>
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
            </li><li class="" openid="DDAB661D2D842BADB052FA61CA9E6139">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/38e591cf1ed8efa83ea56f34bbb88af7.png" alt="花月">
              </div>
              <div class="cn-box">
                <span class="c-n">花月</span>
                <span class="c-n1">济南RW侠</span>
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
            </li><li class="" openid="E1C85A6A65AA4D95E7307650BBF7AEFE">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/2ddaf7b8d271e9ed87a458ec48c946bc.png" alt="小年">
              </div>
              <div class="cn-box">
                <span class="c-n">小年</span>
                <span class="c-n1">厦门VG</span>
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
            </li><li class="" openid="5BD8345514032655E8EED144DDD5D6B3">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/3131a3a52761b06dcb89c5ab7f66e52e.png" alt="风劫">
              </div>
              <div class="cn-box">
                <span class="c-n">风劫</span>
                <span class="c-n1">武汉eStarPro</span>
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
            </li><li class="" openid="F0F65882793C8CB1D58C085BCD522A77">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/fcdd4da0c20422cebc71a35df5a20bfb.png" alt="蓝桉">
              </div>
              <div class="cn-box">
                <span class="c-n">蓝桉</span>
                <span class="c-n1">长沙TES.A</span>
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
            </li><li class="" openid="2D8E2E91721A5FB23C0A3F2542B02650">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/2109f8770f35fe7af93e8e2866bb393d.png" alt="乔兮">
              </div>
              <div class="cn-box">
                <span class="c-n">乔兮</span>
                <span class="c-n1">北京WB</span>
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
            </li><li class="" openid="E20DC214C3065406F4162B17E37030F4">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/7c19f73653eebeb163b7861ce9961e6a.png" alt="花云">
              </div>
              <div class="cn-box">
                <span class="c-n">花云</span>
                <span class="c-n1">济南RW侠</span>
              </div>
            </li></ul>
          <ul id="linkage-right-ul4" style="display: none;"><li class="" openid="1D9FE3C27E1D59E8DAC386A9962F0955">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/faac4faa28d92bddc3e143afdd057921.png" alt="阿改">
              </div>
              <div class="cn-box">
                <span class="c-n">阿改</span>
                <span class="c-n1">佛山DRG</span>
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
            </li><li class="" openid="B60BEC66456FDE26DDF9B6F7BCCE6131">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/f019291412bf15426a5cbc39afd18591.png" alt="冰尘">
              </div>
              <div class="cn-box">
                <span class="c-n">冰尘</span>
                <span class="c-n1">长沙TES.A</span>
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
            </li><li class="" openid="3E716DCD3F100C13FAC1F62A7C588D82">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/f6bfc9197e6dc0dfe8ffcac26544c8b8.png" alt="言梦">
              </div>
              <div class="cn-box">
                <span class="c-n">言梦</span>
                <span class="c-n1">上海EDG.M</span>
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
            </li><li class="" openid="2AE8DD8F971354AEE07F078881E87AE9">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/47767bd2507a965cf4c38eabb91b8e9a.png" alt="久凡">
              </div>
              <div class="cn-box">
                <span class="c-n">久凡</span>
                <span class="c-n1">郑州MTG</span>
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
            </li><li class="" openid="A25A35A18EE5DC93117789871D929E83">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/c887c33254a27e4b6990f4c52f33d9df.png" alt="Cat">
              </div>
              <div class="cn-box">
                <span class="c-n">Cat</span>
                <span class="c-n1">成都AG超玩会</span>
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
            </li><li class="" openid="B9E7045B1D667DD896F3A19BB8126880">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/831ad155e862a0da8c048c80ae873aaf.png" alt="小崽">
              </div>
              <div class="cn-box">
                <span class="c-n">小崽</span>
                <span class="c-n1">杭州LGD.NBW</span>
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
            </li><li class="" openid="8B242820C3F35C0DEFB9F257D4020BC4">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/6031efec47f5ad279253f962635a0ecc.png" alt="星宇">
              </div>
              <div class="cn-box">
                <span class="c-n">星宇</span>
                <span class="c-n1">北京WB</span>
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
            </li><li class="" openid="E8A2A312B6A17CDAA74FF27EBEE1E75A">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/92b982171748e8d0e08e29d817e4d164.png" alt="不弃">
              </div>
              <div class="cn-box">
                <span class="c-n">不弃</span>
                <span class="c-n1">深圳DYG</span>
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
            </li><li class="" openid="6D54271544D17B374436D7189EEBC522">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/eb48fec336a3035bbaff57bda95d65c5.png" alt="阿豆（蒋涛）">
              </div>
              <div class="cn-box">
                <span class="c-n">阿豆（蒋涛）</span>
                <span class="c-n1">广州TTG</span>
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
            </li><li class="" openid="AD5024CF823765963E8F42BDA2EA51DE">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/dee0b1d9815975dc77abc3f6beee2cf6.png" alt="夏竹">
              </div>
              <div class="cn-box">
                <span class="c-n">夏竹</span>
                <span class="c-n1">济南RW侠</span>
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
            </li><li class="" openid="6D24B00C1B9E76BCA81D5D7A01DEA2FB">
              <span class="s-img"> </span>
              <div class="userimg">
                <img src="https://smobatv-pic.tga.qq.com/98b7d418ea608c3f940042b2c9318285.png" alt="笑影">
              </div>
              <div class="cn-box">
                <span class="c-n">笑影</span>
                <span class="c-n1">济南RW侠</span>
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
            </li></ul>
        </div>
    
        <div class="ld-btns-box">
          <span class="ld-btn ld-btn-reset" id="ld-btn-reset">重置</span>
          <span class="ld-btn ld-btn-submit" id="ld-btn-submit">确定（<i>全部队员</i>）</span>
          <span class="ld-btn ld-btn-cancel" id="ld-btn-cancel">取消</span>
        </div>
      </div>

    <!-- Add your scripts here if needed -->

</body>

</html>

'''

# 提取信息并保存到CSV文件
img_info_list = extract_img_info(html_content)
save_to_csv(img_info_list, 'output.csv')
