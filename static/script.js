$(document).ready(function(){
    // $('ul.nav > li').click(function (e) {
    //     e.preventDefault();
    //     $('ul.nav > li').removeClass('active');
    //     $(this).addClass('active');
    // });
    const vditor = new Vditor('vditor', {
        typewriterMode: true,
        counter: 100,
        height: 500,
        hint: {
            emojiPath: 'https://cdn.jsdelivr.net/npm/vditor@1.8.3/dist/images/emoji',
            emojiTail: '<a href="https://hacpai.com/settings/function" target="_blank">设置常用表情</a>',
            emoji: {
                'sd': '💔',
                'j': 'https://unpkg.com/vditor@1.3.1/dist/images/emoji/j.png',
            },
        },
        tab: '\t',
        upload: {
            accept: 'image/*,.wav',
            token: 'test',
            url: '/api/upload/editor',
            linkToImgUrl: '/api/upload/fetch',
            filename (name) {
                return name.replace(/[^(a-zA-Z0-9\u4e00-\u9fa5\.)]/g, '').
                replace(/[\?\\/:|<>\*\[\]\(\)\$%\{\}@~]/g, '').
                replace('/\\s/g', '')
            },
        }
    });
});

