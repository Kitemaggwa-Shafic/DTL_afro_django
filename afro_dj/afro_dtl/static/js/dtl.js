// function hide expects an argument / variable target and we find its id
// 
function hide(target){
    var target = document.getElementById(target);
    target.setAttribute("style", "display:none;");
}


// This JS script here is for timing my bootstrap alert messages for 5s only and disappear 
  
    // the `id` attribute of element of div i wanna time out is `message_container`.
    var message_element = document.getElementById("message_container");
    setTimeout(function() {
        message_element.style.display = "none";
    }, 5000); // My timeout is 5 sec for now
 