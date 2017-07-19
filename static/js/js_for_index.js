// vue script
var app = new Vue({
    el: '#vue',
    delimiters: ["{[", "]}"],

    data: {
        // 单选
        style: 'normal',
        // 多选
        features: ['bg', 'road'],
        // 颜色文本框
        color: ['#20A0FF', '#13CE66', '#F7BA2A', '#FF4949'],
        // 右侧表格
        table: '请上传表格。'
    },

    methods: {
        // 单选 改变样式
        setMapStyle: function () {
            map.setMapStyle('amap://styles/' + this.style)
        },

        // 多选 选择图层
        setFeatures: function () {
            map.setFeatures(this.features)
        },

        // 上传文件 绘制标记
        uploadSuccess: function (data) {
            // 显示表格
            this.table = data['table'];

            // 在地图上添加标记
            AMapUI.loadUI(['overlay/SvgMarker'], function (SvgMarker) {
                // 定义4种颜色的形状
                var shape = [];
                [0, 1, 2, 3].forEach(function (i) {
                    shape[i] = new SvgMarker.Shape.Circle({
                        radius: 12,
                        fillColor: app.color[i], //填充色
                        strokeWidth: 0 //描边宽度
                    })
                });


                // 绘制标记
                data['json'].forEach(function (each) {
                    var marker = new SvgMarker(
                        // 选择颜色
                        shape[parseInt(each['color'])],
                        // 其他属性
                        {
                            // 编号
                            iconLabel: {
                                innerHTML: each['no'],
                                style: {color: 'white'}
                            },
                            // 坐标
                            position: [each['lng'], each['lat']]
                        });
                    marker.setMap(map)

                });
            })
        }
    }
});

// 显示高德地图
var map = new AMap.Map('amap', {
    zoom: 11,
    center: [118.8, 32.1]
});