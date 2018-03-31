//评分
function star(){
	var grade_1=$(".body_middle_book_grade_num_1").html();
	
	grade_1=(grade_1-0)/2;
	var grade_1_star1=Math.floor(grade_1)

	for(var i=0;i<grade_1_star1;i++)
	{

		$(".body_middle_book_grade_star_1").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_1_star2=grade_1-0-grade_1_star1;
	
	if(grade_1_star2!=0){
		$(".body_middle_book_grade_star_1").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}
	
//////////////////////////////////////////////////
	var grade_2=$(".body_middle_book_grade_num_2").html();
	
	grade_2=(grade_2-0)/2;
	
	var grade_2_star1=Math.floor(grade_2)

	for(var i=0;i<grade_2_star1;i++)
	{

		$(".body_middle_book_grade_star_2").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_2_star2=grade_2-0-grade_2_star1;
	
	if(grade_2_star2!=0){
		$(".body_middle_book_grade_star_2").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}

	//////////////////////////////////////////////////
	var grade_3=$(".body_middle_book_grade_num_3").html();
	
	grade_3=(grade_3-0)/2;
	var grade_3_star1=Math.floor(grade_3)
	
	for(var i=0;i<grade_3_star1;i++)
	{

		$(".body_middle_book_grade_star_3").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_3_star2=grade_3-0-grade_3_star1;
	if(grade_3_star2!=0){
		$(".body_middle_book_grade_star_3").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}
		//////////////////////////////////////////////////
	var grade_4=$(".body_middle_book_grade_num_4").html();
	
	grade_4=(grade_4-0)/2;
	var grade_4_star1=Math.floor(grade_4)
	
	for(var i=0;i<grade_4_star1;i++)
	{

		$(".body_middle_book_grade_star_4").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_4_star2=grade_4-0-grade_4_star1;
	if(grade_4_star2!=0){
		$(".body_middle_book_grade_star_4").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}
		//////////////////////////////////////////////////
	var grade_5=$(".body_middle_book_grade_num_5").html();
	
	grade_5=(grade_5-0)/2;
	var grade_5_star1=Math.floor(grade_5)
	
	for(var i=0;i<grade_5_star1;i++)
	{

		$(".body_middle_book_grade_star_5").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_5_star2=grade_5-0-grade_5_star1;
	if(grade_5_star2!=0){
		$(".body_middle_book_grade_star_5").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}
}
star();

//点赞变红
// for(var n=1;n<=5;n++)
// {
// 	$(".body_middle_book_like_"+n).click(function(){

// console.log(".body_middle_book_like_"+n);
// 	$(".body_middle_book_like_"+n).find("img").attr('src','../images/love_red.png');
// });
// }
// $(".body_middle_book_like_1").click(function(){
	

// 	$(".body_middle_book_like_1 img").attr('src','../images/love_red.png');
// });
// $(".body_middle_book_like_2").click(function(){
	

// 	$(".body_middle_book_like_2 img").attr('src','../images/love_red.png');
// });
// $(".body_middle_book_like_3").click(function(){


// 	$(".body_middle_book_like_3 img").attr('src','../images/love_red.png');
// });
// $(".body_middle_book_like_4").click(function(){
	

// 	$(".body_middle_book_like_4 img").attr('src','../images/love_red.png');
// });
// $(".body_middle_book_like_5").click(function(){
	


// 	$(".body_middle_book_like_5 img").attr('src','../images/love_red.png');
// });
var love_2=new Array(0,0,0,0,0);
// for(var i=0;i<5;i++)
// {
// 	$(".body_middle_book_like_"+).eq(0).click(function(){
// 	// $(this).index();

//   	love_2[0]+=1;
//   if(love_2[0]%2!=0)
//   {
//     $(this).find("img").attr({'src':'../images/grade_love.png'});
//   }
//   else{
//     $(this).find("img").attr({'src':'../images/love_white.png'});
//   }
// })
// }
$(".body_middle_book_like_1").eq(0).click(function(){
	// $(this).index();

  	love_2[0]+=1;
  if(love_2[0]%2!=0)
  {
    $(this).find("img").attr({'src':'../images/grade_love.png'});
  }
  else{
    $(this).find("img").attr({'src':'../images/love_white.png'});
  }
})
$(".body_middle_book_like_2").eq(0).click(function(){
	// $(this).index();
	
  	love_2[1]+=1;
  if(love_2[1]%2!=0)
  {
    $(this).find("img").attr({'src':'../images/grade_love.png'});
  }
  else{
    $(this).find("img").attr({'src':'../images/love_white.png'});
  }
})
$(".body_middle_book_like_3").eq(0).click(function(){
	// $(this).index();
	
  	love_2[3]+=1;
  if(love_2[3]%2!=0)
  {
    $(this).find("img").attr({'src':'../images/grade_love.png'});
  }
  else{
    $(this).find("img").attr({'src':'../images/love_white.png'});
  }
})
$(".body_middle_book_like_4").eq(0).click(function(){
	// $(this).index();
	
  	love_2[4]+=1;
  if(love_2[4]%2!=0)
  {
    $(this).find("img").attr({'src':'../images/grade_love.png'});
  }
  else{
    $(this).find("img").attr({'src':'../images/love_white.png'});
  }
})
$(".body_middle_book_like_5").eq(0).click(function(){
	// $(this).index();
	
  	love_2[2]+=1;
  if(love_2[2]%2!=0)
  {
    $(this).find("img").attr({'src':'../images/grade_love.png'});
  }
  else{
    $(this).find("img").attr({'src':'../images/love_white.png'});
  }
})
// $(document).ready(function() {  
//     $(".tipsClass3").hover(function() {  
//         $(this).find(".tipstutorials").animate({  
//             opacity: "show",  
//             top: "280",//此处可以设置弹窗属性  
//         width:"180",  
//             height:"68",   
//             left: "50"  
//         }, "slow");  
//     }, function() {  
//         $(this).find(".tipstutorials").animate({  
//             opacity: "hide",  
//             top: "160"  
//         }, "fast");  
//     });  
// }); 

//头部固定
$(document).ready(function(){  
    var a,b,c;  
    a = $(window).height();    //浏览器窗口高度  
    var group = $(".body_middle_book_list");  
    $(window).scroll(function(){  
        b = $(this).scrollTop();   //页面滚动的高度  
        c = group.offset().top;

          //元素距离文档（document）顶部的高度
          // console.log("a="+a);
          // console.log("b="+b);
          // console.log("c="+c);  
        if(b>c){  
           $(".body_top").css("position","fixed");
           $(".body_top").css("top","0");
           $(".body_top").css("z-index","99");
           $(".container").height(1916);


        }else{  
           $(".body_top").css("position","static"); 
           $(".container").height(2000);
           $(".body_top").css("z-index","auto");
        }  
    });  
}); 


$(".body_top_nav_list li").mouseenter(function(){
	$(this).find("div").css('display','block');
	console.log("999");
	$("body_top_nav_1").find("div").css('display','block');
});
$(".body_top_nav_list li").mouseleave(function(){
	$(this).find("div").css('display','none');
	$(".body_top_nav_1").find("div").css('display','block');
});


//搜索框
$(".search_box_input").click(function(){
  $(this).attr("value","");
});
$(".search_box_input").blur(function(){
  $(this).attr("value","请输入关键词");
});