//3、（字符）检查文件上传表单控件，如果含有[jpg,jpeg,gif,png]则显示“文件类型合法”，否则“显示文件类型错误”
 
$(".logo_2").animate({'opacity':'1','margin-top':'48'},2000);
$(".body").find("h3").animate({'opacity':'1'},2000);

function checkFileExt(filename)
{
 var flag = false; //状态
 var arr = ["jpg","png","gif"];
 //取出上传文件的扩展名
 var index = filename.value.lastIndexOf(".");
 var ext = filename.value.substr(index+1);
 //循环比较
 for(var i=0;i<arr.length;i++)
 {
  if(ext == arr[i])
  {
   flag = true; //一旦找到合适的，立即退出循环
   break;
  }
 }
 //条件判断
 if(flag)
 {
  // document.write("文件名合法");
 }else
 {
  alert("文件名不合法");
  filename.value = "";
  return false;
 }
}

// $(".personal_change_sign_input textarea").each(function(){

// 	var comment_length = $(this).val().length ;
// 	if( comment_length >30){
// 		$(this).val($(this).val().substring(0,30))

// 	}
// })
function checkenter(){
	$(".personal_change_sign_input textarea").keydown(function(event){

	if(event.keyCode == 13 || event.keyCode == 32)
	{
	window.event.returnValue = false;
	}
	else{
		var comment_length = $(".personal_change_sign_input textarea").val().length ;
	if( comment_length >25){
		$(this).val($(this).val().substring(0,25))
	}
	}
	})

	
}

// 	$(".personal_body_perinfo_write").click(function(){
// 	$(".personal_body_perinfo_words").removeAttr('disabled');
// 	$(".personal_body_perinfo_words").removeProp('border')
// 	console.log("666")
// 	$(".personal_body_perinfo_words").focus();

// });
// $(".personal_body_perinfo_words").blur(function(){
// 	$(this).attr('disabled','disabled');
// 	$(this).css({'border':'none'})
	
// });
$(".regist_form_name_input").keydown(function(){
	if($(this).val().length>7)
{
	$(".regist_form_name_input_tip").show();
	$(this).val($(this).val().substring(0,7))
}
else{
	$(".regist_form_name_input_tip").hide();
}

	
}
)

$(".regist_form_name_input").keyup(function(){
	if($(this).val().length<=7)
{
	$(".regist_form_name_input_tip").hide();
}

	
}
)
$(".regist_form_name_input").blur(function(){

	$(".regist_form_name_input_tip").hide();
	

	
}
)



var url_2,url_1,url_af,url_3;
var sign_and;
var sign_choose;
var flag = true;
function aaa(){
	var url_val = window.location.href;
	var url_length = url_val.length;

	sign_choose = url_val.lastIndexOf("?");
    sign_and= url_val.lastIndexOf("&");
    url_3= url_val.substring(0,sign_choose+1);
    url_2= url_val.substring(sign_and,url_length);
    url_1 = url_val.substring(sign_choose+6,sign_and);
    // url_4= $(".ccc").val().substring(sign_and+1,url_length);
    //状态
	 
	 	var regPos = /^\d+(\.\d+)?$/; //非负浮点数
	 
	 	//循环比较

	 	if(regPos.test(url_1) != true)
		{

			flag = false;
		}
	  

		url_af = url_3+"page=1"+url_2
	}
	

// aaa();