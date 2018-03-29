$(".body_top_nav_list li").mouseenter(function(){
	$(this).find("div").css('display', 'block');
	$("body_top_nav_1").find("div").css('display', 'block');
});
$(".body_top_nav_list li").mouseleave(function(){
	$(this).find("div").css('display', 'none');
	$(".body_top_nav_1").find("div").css('display', 'block');
});

//头部固定
$(document).ready(function(){  
    var a,b,c;  
    a = $(window).height();    //浏览器窗口高度  
    var group = $(".body_middle_article_page_1");  
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


var time_set=true;
var now_page=0;
var total_page=1;
//下一页

$(".next_page").click(function(){
  if(now_page<total_page){

  now_page+=1;

  $(".body_middle_inner ul").eq(now_page).css({'display':'block'});
  $(".body_middle_inner ul").eq(now_page).siblings().css({'display':'none'});
  }
 else{
    

    if(time_set==true)
  {

    time_set=false;
    $(".last_page_tip").fadeIn();
      var time_1=setInterval(function(){


      },2000) 

    $(".last_page_tip").delay(1000).fadeOut(function(){
      clearInterval(time_1);
      time_set=true;

    });
    
  } 
}

});

//上一页

$(".last_page").click(function(){
  if(now_page>0){ 
    now_page-=1;
    $(".body_middle_inner ul").eq(now_page).css({'display':'block'});
    $(".body_middle_inner ul").eq(now_page).siblings().css({'display':'none'});
  }
  else{
        if(time_set==true)
     {

      time_set=false;
      $(".first_page_tip").fadeIn();
      var time_2=setInterval(function(){
        // time_set=true;

        },2000) 
      // $(".last_page").css({'disabled':'true'});
      
      $(".first_page_tip").delay(1000).fadeOut(function(){
        clearInterval(time_2);
        time_set=true;

        // console.log(time_set);
      });

    }
}

  });
  
//首页
$(".first_page").click(function(){
now_page=0;
 if(now_page>0){ 
    now_page-=1;
    $(".body_middle_inner ul").eq(now_page).css({'display':'block'});
    $(".body_middle_inner ul").eq(now_page).siblings().css({'display':'none'});
  }
  else{
        if(time_set==true)
     {

      time_set=false;
      $(".first_page_tip").fadeIn();
      var time_2=setInterval(function(){
        // time_set=true;

        },2000) 
      // $(".last_page").css({'disabled':'true'});
      
      $(".first_page_tip").delay(1000).fadeOut(function(){
        clearInterval(time_2);
        time_set=true;

        // console.log(time_set);
      });

    }
    else{
      $(".body_comment_content ul").eq(now_page).css({'display':'block'});
$(".body_comment_content ul").eq(now_page).siblings().css({'display':'none'});
    }

}
});



//搜索框
$(".search_box_input").focus(function(){
  $(this).attr("value","");
  $(this).css('color','black');

  
});
$(".search_box_input").blur(function(){
var content = $(this).val();
  if( $(this).val() == ""){
    
    $(this).attr("value","请输入关键词");
    $(this).css('color','#C9C9C9');
  }

});

//点赞
var time_set2=true;

$(".body_middle_article_like_1").click(function(){

    $(this).find("img").attr({'src':'../images/grade_love.png'});

   
     if(time_set2==true)
     {

      time_set2=false;
      $(".article_save_tip").fadeIn();
      var time_3=setInterval(function(){
     

        },2000) 
  
      
      $(".article_save_tip").delay(1000).fadeOut(function(){
        clearInterval(time_3);
        time_set2=true;

       
      });
    }

})

