
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
   var content=$(this).val();
  	if(content==""){
  		$(this).css({'color':'#C9C9C9'});
  		$(this).attr("value","请输入正确的邮箱地址");
	}
	else{
		$(this).css({'color':'black'});
	}

});


//错误提示
var name_wrong = false;
var code_wrong = false;
var jump = true;
if(name_wrong == true)
{
  $(".login_form_name_tip").show();
}
else
{
  $(".login_form_name_tip").hide();
}

if(code_wrong == true)
{
  $(".login_form_code_tip").show();
}
else
{
  $(".login_form_code_tip").hide();
}

$(".login_form_verify_button").click(function(){
  if(jump == true)
{
  window.location.href = "../html/shouye.html";
}

});
