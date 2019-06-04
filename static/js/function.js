///////////////////////////// * * ALL FUNCTION ** ///////////////////////////
////////*********Display and undisplay input field ********/////////

function SwitchInputField(mode) {
  var x = document.getElementById("input-form");
    if (mode === "block") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
}

///////********** Display and undisplay input field  End here ****/////


///////////**     TIME FUNCTION       **//////////////////////////////
function wait(ms)
{
  var d = new Date();
  var d2 = null;
  do { d2 = new Date(); }
  while(d2-d < ms);
}
///////////**     TIME FUNCTION  ENDS HERE     **//////////////////////////////

function FinalMessage(message,facebook,linkedin,twitter,instagram){
  $(".media-list").append('<li class="right clearfix"><span class="chat-img pull-right">\
                  </span><div class="chat-body clearfix">\
                  <div class="header">\
                  </div>\
                  <p class="pull-left"><font color ="red">'+message+'</font></p>\
                  <div class="pull-left"><font color="black"><a href="'+facebook+'">Facebook</a><br>\
                  <div class="pull-left"><font color="black"><a href="'+linkedin+'">Linkedin</a><br>\
                  <div class="pull-left"><font color="black"><a href="'+twitter+'">Twitter</a><br>\
                  <div class="pull-left"><font color="black"><a href="'+instagram+'">Instagram</a><br>\
               </div>\
          </li>');
  $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
}

function BotRespond(respond,bot_name){
  $(".media-list").append('<li class="right clearfix"><span class="chat-img pull-right">\
                  <img src="http://placehold.it/50/FA6F57/fff&text='+bot_name+'" alt="User Avatar" class="img-circle" />\
              </span>');
  ////// *** TEMP IMG URL NEED TO CHANGE ONCE PUBLISHED *** /////////

  $(".media-list").append('<div class="chat-body clearfix">\
                  <div class="header">\
                  </div>\
                  <p class="pull-left"><font color ="red">'+respond+'</font></p>\
               </div>\
          </li>');
  $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
}

function BotPreMessage(message){
  $(".media-list").append('<li class="right clearfix"></span>\
              <div class="chat-body clearfix">\
                  <div class="header">\
                  </div>\
                  <p class="pull-left"><font color ="red">'+message+'</font></p>\
               </div>\
          </li>');
  $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
}

function BotPostMessage(message){
  $(".media-list").append('<li class="right clearfix"></span>\
              <div class="chat-body clearfix">\
                  <div class="header">\
                  </div>\
                  <p class="pull-left"><font color ="red">'+message+'</font></p>\
               </div>\
          </li>');
  $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
}

function BotQuestion(ques){
  $(".media-list").append('<li class="right clearfix"></span>\
              <div class="chat-body clearfix">\
                  <div class="header">\
                  </div>\
                  <p class="pull-left"><font color ="red">'+ques+'</font></p>\
               </div>\
          </li>');
  $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
}

function UserRespond(response){
  $( ".media-list" ).append('<li class="left clearfix"><span class="chat-img pull-left">\
                          <img src="http://placehold.it/50/55C1E7/fff&text=You" alt="User Avatar" class="img-circle" />\
                      </span>\
                      <div class="chat-body clearfix">\
                          <div class="header">\
                              </div>\
                              <p class="pull-right"><font color="blue">'+response+'</font></p>\
                          </div>\
                      </li>');
  $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
}

function display_option(option){
  optional_div = '<div class="quest-tag"><form method="post" id="searchFormSPECIAL">';
  for (i = 0; i < option.length; i++){
    optional_div = optional_div + '<label><input type="checkbox" name="selector" value="'+option[i]+'">'+option[i]+'</label>'
  }
  optional_div = optional_div + '  <input type="submit" value="Confirm" /></form></div>'
  //$('.media-list').append(optional_div);
  return optional_div
}

function FormDisplay(option){
  $(".media-list").append(option);
  $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
  return
}


function initial_message(bot_name,bot_image,welcome_msg){
  console.log(bot_image)
  var initial_form = '<div>'+welcome_msg+'</div>\
                    <img src="'+bot_image+'" alt="" style="float:none;height: auto;width:20%">';
   $('.media-list').append(initial_form);

   var ques_part = '<div class="right clearfix"><span class="chat-img pull-right">\
                    <img src="http://placehold.it/50/FA6F57/fff&text='+bot_name+'" alt="User Avatar" class="img-circle" />\
               </span>\
               <div class="chat-body clearfix">\
                   <div class="header">\
                       <small class=" text-muted"></small>\
                   </div>\
                </div>\
           </div>';
  $('.media-list').append(ques_part);
    $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
  return
}


function append_question(ques,bot_name){
  var ques_part = '<div class="right clearfix"><span class="chat-img pull-right">\
                  </span>\
              <div class="chat-body clearfix">\
                  <div class="header">\
                      <small class=" text-muted"></small>\
                      <strong class="pull-right primary-font">'+bot_name+'</strong>\
                  </div>\
               </div>\
          </div>';

      $(".panel-body").stop().animate({ scrollTop: $(".panel-body")[0].scrollHeight}, 1000);
    $('.media-list').append(ques_part);
}


////////////////////////// *** FUNCTION END HERE ***///////////////////////////
