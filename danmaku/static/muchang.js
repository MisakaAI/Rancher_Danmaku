// 编辑时变为成黑色
function Edit(x) {
    if (x.value == x.defaultValue) {
        x.value = ''
        x.style.color = 'rgba(0,0,0,0.8)'
    } else if (x.value == '') {
        x.value = x.defaultValue
        x.style.color = 'rgba(0,0,0,0.5)'
    }
}
// 检查表单
function check() {
    var result = true
    var a = document.getElementsByName('id')[0].value
    var b = document.getElementsByName('id')[0].defaultValue
    if ( a == b ) {
        result = false
    }
    return result
}