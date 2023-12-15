function drawCartoon() {
    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
        graphic: {
            elements: [
            {
                type: 'text',
                left: 'center',
                top: 'center',
                style: {
                text: 'KPL Data Visualization',
                fontSize: 80,
                fontWeight: 'bold',
                lineDash: [0, 200],
                lineDashOffset: 0,
                fill: 'transparent',
                stroke: '#000',
                lineWidth: 1
                },
                keyframeAnimation: {
                duration: 1000,
                loop: false,
                keyframes: [
                    {
                    percent: 0.7,
                    style: {
                        fill: 'transparent',
                        lineDashOffset: 200,
                        lineDash: [200, 0]
                    }
                    },
                    {
                    // Stop for a while.
                    percent: 0.8,
                    style: {
                        fill: 'transparent'
                    }
                    },
                    {
                    percent: 1,
                    style: {
                        fill: 'black'
                    }
                    }
                ]
                }
            }
            ]
        }
    };

    option && myChart.setOption(option);
}

document.addEventListener('DOMContentLoaded', function() {
    drawCartoon()
});
