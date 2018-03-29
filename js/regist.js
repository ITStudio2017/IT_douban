//logo 变化


$(".logo_2").animate({'opacity':'1','margin-top':'48'},2000);
$(".body").find("h3").animate({'opacity':'1'},2000);
//

//input 
$(".regist_form_verify_input").focus(function(){
  $(this).attr("value","");
  $(this).css({'color':'black'});

  
});
$(".regist_form_verify_input").blur(function(){
  // $(this).attr("value","请输入正确的邮箱地址");
  $(this).css({'color':'#C9C9C9'});

});

//input 2
$(".regist_form_name_input").focus(function(){
  $(this).attr("value","");
  $(this).css({'color':'black'});

  
});
$(".regist_form_name_input").blur(function(){
  // $(this).attr("value","请输入正确的邮箱地址");
  // $(this).css({'color':'#C9C9C9'});
    var content=$(this).val();
  if(content==""){
  		$(this).css({'color':'#C9C9C9'});
  		$(this).attr("value","请输入正确的邮箱地址");
	}
	else{
		$(this).css({'color':'black'});
	}

});

//input code


$(".regist_form_code_again_input").focus(function(){
	console.log("666");
  $(this).attr("value","");
  $(this).css({'color':'black'});

  
});
$(".regist_form_code_again_input").blur(function(){
  //判断用户是否输入，如果没有输入继续显示提示部分
  var content=$(this).val();
  if(content==""){
  		$(this).css({'color':'#C9C9C9'});
  		$(this).attr("value","请再次输入密码");
	}
	else{
		$(this).css({'color':'black'});
	}

});
