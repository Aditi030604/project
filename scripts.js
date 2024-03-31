$(document).ready(function(){
    $('#recurring-checkbox').change(function() {
        if ($(this).is(":checked")) {
            $('#recurring-days').show();
        } else {
            $('#recurring-days').hide();
        }
    });

    $('#alarm-form').submit(function(event){
        event.preventDefault();
        var alarmTime = $('#alarm-time').val();
        var recurringDays = [];
        $('input[name="recurring_days[]"]:checked').each(function() {
            recurringDays.push($(this).val());
        });
        $.ajax({
            type: 'POST',
            url: '/set-alarm',
            data: {alarm_time: alarmTime, recurring_days: recurringDays}, // corrected the key name
            success: function(response){
                console.log(response.message);
                // Display a notification when the alarm is successfully set
                alert(response.message); // Change this to use a notification library for a nicer UI
            },
            error: function(xhr, status, error){
                console.error(error);
                alert('Error occurred while saving the alarm.');
            }
        });
    });
});
