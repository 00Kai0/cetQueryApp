//打开字滑入效果
window.onload = function(){
	$(".connect p").eq(0).animate({"left":"0%"}, 600);
	$(".connect p").eq(1).animate({"left":"0%"}, 400);
};
//jquery.validate表单验证
$(document).ready(function(){
	//登陆表单验证



	$("#loginForm").validate({
		rules:{
			username:{
				required:true,//必填
				minlength:10, //最少10个字符
			},
            selProvince:{
				required:true,
				//minlength:1,
			},
            password:{
                required:true,
                minlength:13,
            },
		},
		//错误信息提示
		messages:{
			username:{
				required:"请输入学号",
				minlength:"请输入10位学号",
				remote: "用户名已存在",
			},
            selProvince:{
				required:"请选择",
				//minlength:"请选择",
			},
            password:{
                required:"请输入",
                minlength:"密码至少为13个字符",
            },
		},
	});
	//注册表单验证
	$("#registerForm").validate({
		rules:{
			username:{
				required:true,//必填
				minlength:1, //最少1个字符
				remote:{
					url:"http://kouss.com/demo/Sharelink/remote.json",//用户名重复检查，别跨域调用
					type:"post",
				},
			},
			password:{
				required:true,
				minlength:10,
			},
            phone_number:{
                required:true,
                minlength:13,
            },
		},
		//错误信息提示
		messages:{
			username:{
				required:"请输入姓名",
				minlength:"姓名至少为1个字符",
				maxlength:"姓名至多为40个字符",
				remote: "姓名已存在",
			},
			password:{
				required:"请输入学号",
				minlength:"学号为10位",
			},
            phone_number:{
                required:"请输入准考证号",
                //digits:"请输入10位学号",
                minlength:"准考证号为13位/15位",
            },
		},
	});
});