$(".personal_body_write_content").click(function(){
	$(".personal_body_write_content_tip").css('display', 'none');
	$(".personal_body_write_title_input").attr('value','#请在此添加标题');
	$(".personal_body_write_add_img_tip").css('display','block');
});
$(".personal_body_write_add_img").click(function(){
	$(".personal_body_write_add_img_tip").css('display', 'none');
	$(".personal_body_write_title_input").attr('value','#请在此添加标题');
	$(".personal_body_write_content_tip").css('display','block');

});
$(".personal_body_write_title_input").click(function(){
	$(".personal_body_write_content_tip").css('display', 'block');
	$(".personal_body_write_title_input").attr('value','');
	$(".personal_body_write_add_img_tip").css('display','block');
});