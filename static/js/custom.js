///////////////////////////////////////////////////////////////////////////
$(document).ready( function () {
  initial_message(bot_name,bot_image,welcome_msg);
  bot_reply = response;
  var unique_id = 'abc123';
  var url = "/ask/"+unique_id;
  //append_question(ques,bot_name);
  console.log(ques);
  BotQuestion(ques);
  $(document).on('submit', '#searchFormSPECIAL', function (event) {
  /* stop form from submitting normally */
      event.preventDefault();
      var query_text = [];
      console.log(typeof(lead));
      console.log(lead);
      $.each($("input[name='selector']:checked"), function(){
            query_text.push($(this).val());
          });
      console.log("selected elements" + query_text.join(", "));
      UserRespond(query_text);
      lead[value] = query_text;
      console.log(lead);
      // console.log(value);
      // console.log(bot_reply);
      wait(400);
      BotRespond(bot_reply,bot_name);
      //console.log(event);
      //BotRespond(response);
      var my_text = query_text.toString();
    //  console.log(my_text);
      if(count == limit){
        //console.log(lead);
        $.ajax({
          type:"POST",
          url:"/submit",
          dataType:'json',
          success: function(response){
            console.log(response);
            var message = response.message;
            var facebook = response.facebook;
            var linkedin = response.linkedin;
            var twitter = response.tweet;
            var instagram = response.insta;
            console.log(message);
          },
          error: function(error){
          console.log(error);
        }
        });
      }
      else{
        $.ajax({
          type: "POST",
          url: url,
          data: {chatmessage:my_text,count:count},
          dataType:'json',
          success: function(response) {
              //console.log(response)
              var answer = response.answer;
              var ques = response.ques;
              var option = response.option;
              bot_reply = response.response;
              // console.log(option);
              // console.log(option.length);
              // console.log("testing");
              wait(400);
              BotQuestion(ques);
              if (option.length>0){
                option = display_option(option);
                FormDisplay(option);
                //SwitchInputField("block");
              }
              else{
                //SwitchInputField("none");
              }

                  value = response.value;

              const chatPanel = document.getElementById("chatPanel");

          },
          error: function(error) {
              console.log(error);
          }
        });
    }
      $('.quest-tag').remove();
      count = count+1;
  });


  ////////////////////////* TEXT INPUT FIELD FUNCTION START *////////////////////////////

  $(function(){
      $( "#btn-chat" ).click(function( event ) {
        event.preventDefault();
        $("#form-chat").submit();
    });
      $("#form-chat").submit(function(event){
        console.log("from button click")
          console.log(url);
          event.preventDefault();
          var pesan =$("#chatmessage").val();
          UserRespond(pesan);
          lead[value] = pesan;
          console.log(lead);

          // console.log(bot_reply);
          // console.log(response);

          if(count == limit+1){

            console.log(typeof(lead));
            $.ajax({
              data:JSON.stringify({lead:lead}),
              type:"POST",
              url:"/submit",
              dataType:'json',
              contentType: "application/json",
              success: function(response){
                console.log(response);
                $('#chatmessage').val('');
                wait(400);
                BotRespond(bot_reply,bot_name);
                var message = response.message;
                var facebook = response.facebook;
                var linkedin = response.linkedin;
                var twitter = response.tweet;
                var instagram = response.insta;
                FinalMessage(message,facebook,linkedin,twitter,instagram);
                console.log(count);
                console.log(limit);
              },
              error: function(error){
              console.log(error);
            }
            });

          }else if (count>limit+1) {
            $.ajax({
              type:"POST",
              url:"/askbot",
              data: $(this).serialize(),
              success: function(response){
                console.log(response);
                $('#chatmessage').val('');
                var bot_answer = response.answer;
                wait(400);
                BotRespond(bot_answer,bot_name);
              },
              error: function(error){
              console.log(error);
            }
            });

          }
          else {
            $('#chatmessage').val('');
            $.ajax({
                type: "POST",
                url: url,
                data: {chatmessage:pesan,count:count},
                dataType:'json',
                success: function(response) {
                    console.log(response)
                    var answer = response.answer;
                    $('#chatmessage').val('');
                    var option = response.option;
                    wait(400)
                    BotRespond(bot_reply,bot_name);
                    bot_reply = response.response;
                    value = response.value;
                  //  console.log(bot_reply);
                    var ques = response.ques;
                    wait(400);
                    BotQuestion(ques);
                    // console.log(option);
                    // console.log(option.length);
                    if (option.length>0){
                      option = display_option(option);
                      FormDisplay(option);
                      //SwitchInputField("block");
                    }else {
                      //SwitchInputField("none");
                    }
                    const chatPanel = document.getElementById("chatPanel");
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
          count = count + 1;

      });

  });


  ////////////////////////* TEXT INPUT FIELD FUNCTION START *////////////////////////////
});
