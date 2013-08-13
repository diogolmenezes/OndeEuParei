$(document).ready(function(){
    $('.popup').click(function(){
        window.open($(this).attr('href'),'popup','width=400,height=300')
        return false;
    });
});