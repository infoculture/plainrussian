<?
error_reporting(E_ERROR);

$type = $_POST['type'];
$target = $_POST['value'];

if($type == 'url') {
	if(mb_substr($target, 0, 4) != 'http') {
		$target = 'http://' . $target;
	}

} elseif($type == 'text') {
	$target = strip_tags($_POST['value']);

} else {
	exit;
}


if(!$data = get_data($target, $type)) {
	echo '<span>Извините, сервер недоступен</span>';
	exit;
}


function get_data($target, $type) {
	$target = urlencode($target);
//	$url = 'http://' .$_SERVER['HTTP_HOST'] . '/data.txt'; //Удалить

	$ch = curl_init();
	if ($type == 'text')
	{
	    $url = "http://api.plainrussian.ru/api/1.0/ru/measure/";
	    curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, "{$type}={$target}");	    
	}
	else
	{
    	$url = "http://api.plainrussian.ru/api/1.0/ru/measure/?{$type}={$target}";
	};
	curl_setopt($ch, CURLOPT_URL,$url);
	curl_setopt($ch, CURLOPT_FAILONERROR, 1);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);
	curl_setopt($ch, CURLOPT_TIMEOUT, 3);
	$result = curl_exec($ch);
	curl_close($ch);

	return json_decode($result);

}
?>

<div class="bs-callout bs-callout-info">
	<p>Уровень читабельности: <b><?=round($data->indexes->index_SMOG, 2)?></b></p>
	<p>Аудитория: <?=$data->indexes->grade_SMOG?></p>
</div>

<? if($type == 'url'): ?>
	<a href="/#url=<?=urlencode($_POST['value'])?>">Ссылка на отчет</a>
<? endif; ?>

<h3>Индикаторы читаемости текста</h3>
<table class="table table-condensed">
	<tr>
		<td>Flesch-Kincaid</td>
		<td><?=round($data->indexes->index_fk, 2)?></td>
	</tr>
	<tr>
		<td>Coleman-Liau index</td>
		<td><?=round($data->indexes->index_cl, 2)?></td>
	</tr>
	<tr>
		<td>Dale-Chale readability formula</td>
		<td><?=round($data->indexes->index_dc, 2)?></td>
	</tr>
	<tr>
		<td>Automated Readability Index</td>
		<td><?=round($data->indexes->index_ari, 2)?></td>
	</tr>
	<tr>
		<td>SMOG</td>
		<td><?=round($data->indexes->index_SMOG, 2)?></td>
	</tr>
</table>

<h3>Расчетные показатели</h3>
<table class="table table-condensed">
	<tr>
		<td>Число знаков</td>
		<td><?=round($data->metrics->chars, 2)?></td>
	</tr>
	<tr>
		<td>Число пробелов</td>
		<td><?=round($data->metrics->spaces, 2)?></td>
	</tr>
	<tr>
		<td>Число букв</td>
		<td><?=round($data->metrics->letters, 2)?></td>
	</tr>
	<tr>
		<td>Число слов</td>
		<td><?=round($data->metrics->n_words, 2)?></td>
	</tr>
	<tr>
		<td>Число предложений</td>
		<td><?=round($data->metrics->n_sentences, 2)?></td>
	</tr>
	<tr>
		<td>Число слов с более чем 4-мя слогами</td>
		<td><?=round($data->metrics->n_complex_words, 2)?></td>
	</tr>
	<tr>
		<td>Число слов до 4-х слогов включительно</td>
		<td><?=round($data->metrics->n_simple_words, 2)?></td>
	</tr>
	<tr>
		<td>Среднее число слов на предложение</td>
		<td><?=round($data->metrics->avg_slen, 2)?></td>
	</tr>
	<tr>
		<td>Среднее число слогов на предложение</td>
		<td><?=round($data->metrics->avg_syl, 2)?></td>
	</tr>
	<tr>
		<td>Процент сложных слов от общего числа</td>
		<td><?=round($data->metrics->c_share, 2)?></td>
	</tr>
</table>
