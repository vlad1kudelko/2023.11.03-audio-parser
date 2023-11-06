import os

urls = [
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/grand-classical',       'grand-classical'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/upright-piano',         'upright-piano'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/organ',                 'organ'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/classical-guitar',      'classical-guitar'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/harp',                  'harp'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/glockenspiel',          'glockenspiel'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/violin',                'violin'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/pan-flute',             'pan-flute'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/accordion',             'accordion'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/sitar',                 'sitar'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/oud',                   'oud'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/mixed-percussion',      'mixed-percussion'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/steel-pan',             'steel-pan'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/brass-ensemble',        'brass-ensemble'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/koto',                  'koto'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/saxophone',             'saxophone'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/clarinet',              'clarinet'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/oboe',                  'oboe'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/flamenco-guitar',       'flamenco-guitar'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/double-bass',           'double-bass'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/auditorium-piano',      'auditorium-piano'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/jazz-piano',            'jazz-piano'],
    #  ['https://virtualpiano.net/wp-content/themes/generatepress_child/js-dev/samples/stage-piano',           'stage-piano'],
    ['https://cdn.autopiano.cn/autopiano/samples/bright_piano', 'test'],
]

os.system('cd out ; rm -rf *')
for url in urls:
    dr = 'out/' + url[1]
    os.system(f'mkdir {dr}')
    for x_3 in [0,1,2,3,4,5,6,7,8,9]:
        for x_1 in 'ABCDEFG':
            for x_2 in ['', 's']:
                os.system(f'cd {dr} ; curl -O {url[0]}/{x_1}{x_2}{x_3}.mp3')
                d = False
                with open(f'{dr}/{x_1}{x_2}{x_3}.mp3') as f:
                    try:
                        if 'xml version=' in str(f.readlines()[0]):
                            d = True
                    except:
                        pass
                if d:
                    os.system(f'rm {dr}/{x_1}{x_2}{x_3}.mp3')
