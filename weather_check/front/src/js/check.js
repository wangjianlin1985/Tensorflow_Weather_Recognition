var IMAGE_URL = '';

function Check() {

}

Check.prototype.listenUploadFileEvent = function () {
    var uploadBtn = $('#upload-btn');
    uploadBtn.change(function () {
        // uploadBtn[0]：找到第一个uploadBtn标签
        // files[0]：files表示可以上传多个文件，在这里只要第一个文件
        var file = uploadBtn[0].files[0];
        var formData = new FormData();
        formData.append('file', file);
        xfzajax.post({
            'url': '/upload_img/',
            'data': formData,
            // 告诉jQuery不需要对文件格式进行处理了
            'processData': false,
            // 使用默认的文件形式，不需要在添加了
            'contentType': false,
            'success': function (result) {
                if (result['code'] === 200) {
                    IMAGE_URL = result['data']['url'];
                    var img_url = result['data']['url'];
                    var imageInput = $('#img-url');
                    imageInput.val(img_url);
                    var inputImg = $('.input-image-file');
                    inputImg.attr('src', img_url)
                }
            }
        })
    })
};


Check.prototype.listenImgCheckEvent = function () {
    var changeBtn = $('#img-change');
    changeBtn.click(function (event) {
        event.preventDefault();
        xfzajax.post({
            'url': '/check_img/',
            'data': {
                'img_url': IMAGE_URL,
            },
            'success': function (result) {
                if (result['code'] === 200) {
                    var check_flower = result['data']['flower'];
                    var check_chance = result['data']['chance'];
                    console.log(check_flower + '概率:' + check_chance);
                    zlalert.alertInfoWithTitle(check_flower, '识别成功!');
                }
                if (result['code'] === 40002) {
                    console.log(result);
                    zlalert.alertErrorToast(result['message'])
                }
                else {
                    console.log(result)
                }
            }
        })
    })
}


Check.prototype.run = function () {
    var self = this;
    self.listenUploadFileEvent();
    self.listenImgCheckEvent();
};


$(function () {
    var check = new Check();
    check.run()
});


