/**
 * converts date to Tue Apr 04 2023, 18:26:48  format
 * @param {string} date
 */
const dateStringTimeConvert = (date) => {
    let new_date = date.split('GMT').shift();
    let myDate = new Date(new_date);
    const time_now  = new Intl.DateTimeFormat('default', {
        hour24: true,
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric'
    }).format(myDate);
    return `${myDate.toDateString()}, ${time_now}`;
}

console.log(dateStringTimeConvert('2023-04-04T19:51:05.584Z'))