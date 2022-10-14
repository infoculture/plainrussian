<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta name='yandex-verification' content='69692685612df50d' />

	<title>Проверка на читабельность текстов | PlainRussian.ru</title>

	<!-- Bootstrap core CSS -->
	<link href="/css/bootstrap.css" rel="stylesheet">

	<!-- Custom styles for this template -->
	<link href="/css/common.css" rel="stylesheet">

	<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
	<!--[if lt IE 9]>
	<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
	<script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
	<![endif]-->
</head>

<body>
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
      js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/ru_RU/sdk.js#xfbml=1&appId=409275065882804&version=v2.0";
          fjs.parentNode.insertBefore(js, fjs);
          }(document, 'script', 'facebook-jssdk'));</script>          


<div class="container">
	<div class="jumbotron">
		<h1>Оценка читабельности текста</h1>
		<p class="lead">"Язык имеет большое значение еще и потому, что с его помощью мы можем прятать наши мысли." <i>Вольтер</i></p>
		<p style="text-align: right;">
<div class="fb-like-box" data-href="https://www.facebook.com/plainrussian" data-width="600" data-height="200" data-colorscheme="light" data-show-faces="true" data-header="false" data-stream="false" data-show-border="true"></div>
	</div>
	<div class="row">
		<ul class="nav nav-pills center-block" id="tabs">
			<li class="active"><a href="#tab-url" data-toggle="tab">URL</a></li>
			<li><a href="#tab-text" data-toggle="tab">Текст</a></li>
		</ul>

		<div class="tab-content">
			<div class="tab-pane fade in active" id="tab-url">
				<div class="input-group">
					<span class="input-group-addon">http://</span>
					<input type="text" id="url" class="form-control" value="<?=$_GET['url']?>">
			    	<span class="input-group-btn">
						<button class="btn btn-success tr-calculate" data-var="url" type="button" data-loading-text="..Загрузка..">Рассчитать</button>
					</span>
				</div>
			</div>
			<div class="tab-pane fade" id="tab-text">
				<textarea id="text" class="form-control" rows="6"></textarea>
				<button class="btn btn-success tr-calculate mr-top pull-right" data-var="text" type="button" data-loading-text="..Загрузка..">Рассчитать</button>
			</div>
		</div>
	</div>

	<div class="row" id="result"></div>

	<hr/>
	<div class="row">
		<div class="col-xs-6">
			<h2>Удобный инструмент проверки текстов</h2>
			<p><b>Инструмент проверки читабельности текстов</b> позволяет определить удобство чтения материалов. Он сработает для сайта, брошюр, руководств и книг. Позволит своевременно внести необходимые исправления при необходимости.			
			</p>
		</div>

		<div class="ol-xs-6">
			<h2>Для кого это?</h2>
			<p>Сервис может быть полезен разработчикам, райтерам, тем кто делает веб-сайты. Сервис нужен всем кто хочет чтобы тексты на страницах были понимаемы, журналистам и всем заинтересованным.</p>
		</div>
  </div>

    <div class="row">
		<div class="col-xs-6">
			<h2>Как это работает</h2>
			<p>Для оценки читабельности текстов используется 5 формул читаемости адаптированных для русского языка. </p>

			<ul>
				<li>Формула Flesch-Kincaid</li>
				<li>Индекс Колман-Лиау</li>
				<li>Automatic Readability Index</li>
				<li>SMOG</li>
				<li>Формула Дэйла-Чейла</li>
			</ul>
		</div>
		<div class="ol-xs-6">
    		<h2>API</h2>
	    	<p>Для тех кто хочет автоматизированно проверять тексты <a href="https://github.com/ivbeg/readability.io/wiki/API">доступно API</a>.</p>
		</div>
		
	</div>
	<div class="row">
	    <div class="col-xs-10">
	    <h2>Поддержать</h2>
	    <p>Ваша помощь очень важна для нас, каждый, даже небольшой взнос пойдет на развитие проекта.</p>
<iframe frameborder="0" allowtransparency="true" scrolling="no" src="https://money.yandex.ru/embed/donate.xml?account=410012648928680&quickpay=donate&payment-type-choice=on&default-sum=500&targets=%D0%9D%D0%B0+%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D1%83+%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0+%22%D0%9E%D1%86%D0%B5%D0%BD%D0%BA%D0%B0+%D1%87%D0%B8%D1%82%D0%B0%D0%B1%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8+%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B0%22&target-visibility=on&project-name=%22%D0%9E%D1%86%D0%B5%D0%BD%D0%BA%D0%B0+%D1%87%D0%B8%D1%82%D0%B0%D0%B1%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8+%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B0%22+(ru.readability.io&project-site=http%3A%2F%2Fru.readability.io&button-text=01&successURL=http%3A%2F%2Fru.readability.io" width="521" height="131"></iframe>
        </div>
	</div>

	<div class="footer">
		<p>&copy; Иван Бегтин (c) 2014. От лица НП "Информационная культура" <a href="http://infoculture.ru">infoculture.ru</a></p>
		<p><!-- Yandex.Metrika informer -->
		<a href="http://metrika.yandex.ru/stat/?id=24037120&amp;from=informer"
		target="_blank" rel="nofollow"><img src="//bs.yandex.ru/informer/24037120/3_1_FFFFFFFF_EFEFEFFF_0_pageviews"
		style="width:88px; height:31px; border:0;" alt="Яндекс.Метрика" title="Яндекс.Метрика: данные за сегодня (просмотры, визиты и уникальные посетители)" onclick="try{Ya.Metrika.informer({i:this,id:24037120,lang:'ru'});return false}catch(e){}"/></a>
		<!-- /Yandex.Metrika informer -->
		
		<!-- Yandex.Metrika counter -->
		<script type="text/javascript">
		(function (d, w, c) {
		    (w[c] = w[c] || []).push(function() {
		            try {
		                        w.yaCounter24037120 = new Ya.Metrika({id:24037120,
		                                            webvisor:true,
		                                                                clickmap:true,
		                                                                                    trackLinks:true,
		                                                                                                        accurateTrackBounce:true});
		                                                                                                                } catch(e) { }
		                                                                                                                    });
		                                                                                                                    
		                                                                                                                        var n = d.getElementsByTagName("script")[0],
		                                                                                                                                s = d.createElement("script"),
		                                                                                                                                        f = function () { n.parentNode.insertBefore(s, n); };
		                                                                                                                                            s.type = "text/javascript";
		                                                                                                                                                s.async = true;
		                                                                                                                                                    s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//mc.yandex.ru/metrika/watch.js";
		                                                                                                                                                    
		                                                                                                                                                        if (w.opera == "[object Opera]") {
		                                                                                                                                                                d.addEventListener("DOMContentLoaded", f, false);
		                                                                                                                                                                    } else { f(); }
		                                                                                                                                                                    })(document, window, "yandex_metrika_callbacks");
		                                                                                                                                                                    </script>
		                                                                                                                                                                    <noscript><div><img src="//mc.yandex.ru/watch/24037120" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
		                                                                                                                                                                    <!-- /Yandex.Metrika counter --></p>
	</div>

</div>



<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="/js/bootstrap.min.js"></script>

<script>
$(function(){
	$('#calculate').button('reset');

	$('.tr-calculate').click(function(){
		var btn = $(this);
		var curr_type = btn.attr('data-var');
		var curr_var = $('#' + btn.attr('data-var'));

		$.ajax({
			type: 'POST',
			url: '/calculate.php',
			data: {type: curr_type, value: curr_var.val()},
			dataType: 'html',
			beforeSend : function (){
				btn.button('loading');
				$('#result').html('');
			},
			success : function (data) {
				$('#result').html(data);
			},
			complete : function (){
				btn.button('reset');
				if(curr_type != 'text')
				{
				   location.hash = '#url=' + curr_var.val(); 
				}
			}
		});
	});

	if(location.hash != '') {
	    var url = location.hash.split('=')[1];
	    document.getElementById("url").value=url;
		$('.tr-calculate[data-var=url]').trigger('click');
	}
})
</script>

</body>
</html>
