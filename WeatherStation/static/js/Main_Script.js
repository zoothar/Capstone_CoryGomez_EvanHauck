/**
 * Created by batman on 3/15/17.
 */


function update(){
    alert_string = '';
        alert_string = alert_string + document.getElementById('datefield1').value;
        alert_string = alert_string + ' ';
        alert_string = alert_string + document.getElementById('datefield2').value;

        alert(alert_string);
}
