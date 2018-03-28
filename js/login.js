
//验证码切换
$(".login_form_verify_image").click(function(){

	$(this).css("background-image",'url("../images/book_list_logo.png")');
})

//logo 变化

$(".logo_2").animate({'opacity':'1','margin-top':'48'},2000);
$(".body").find("h3").animate({'opacity':'1'},2000);


//input 
$(".login_form_name_input").focus(function(){
  $(this).attr("value","");
  $(this).css({'color':'black'});

  
});
$(".login_form_name_input").blur(function(){
  // $(this).attr("value","请输入正确的邮箱地址");
  $(this).css({'color':'#C9C9C9'});

});
