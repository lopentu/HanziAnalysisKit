================
hgct
================

This page showcases the `HGCT (Hanzi Glyph Corpus Toolkit)`_, a tool designed for advanced analysis and querying of Chinese text data, demonstrated through a textbook-derived corpus.

.. _HGCT (Hanzi Glyph Corpus Toolkit): https://yongfu.name/hgct/index.html


Installation
================
To starting using HGCT, clone the repository and install the required dependencies.

- Python Version

  .. code-block:: bash

      Python >= 3.0, < 3.11

- Clone Repository

  .. code-block:: bash
    
      git clone git@github.com:lopentu/HanziAnalysisKit.git

- Install Requirement

  .. code-block:: bash
    
      cd HanziAnalysisKit && pip install -r requirements.txt


Quick Start
================

Building the Corpus
-----------------

To prepare your data for use with the HGCT tool, build your corpus from the provided textbook data:


.. code-block:: python

    from textbook import build_corpus

    # Specify your CSV data file and desired output folder
    csv_file = './data/教科書課文.csv'
    folder = "textbook_corpus"

    # Build the corpus
    build_corpus(csv_file, folder)


This will create a `textbook_corpus` folder in your project directory, containing the processed data ready for analysis with HGCT.


Directory Structure
-----------------

After building the corpus, your project directory will be organized as follows:

.. code-block:: bash

      |--- data/
      |    |--- 教科書課文.csv
      |--- textbook/
      |--- textbook_corpus/ # Newly generated
      |--- ...



Demonstration
================

This section provides comprehensive examples demonstrating the capabilities of HGCT for analyzing Chinese text data. Each example includes a brief description and the expected output.


Corpus Reading and Concordancer Initialization
-----------------

Load your corpus and set up the Concordancer for text analysis:

.. code-block:: python

    from hgct import PlainTextReader, Concordancer

    # Load the corpus into PlainTextReader
    corpus = PlainTextReader(dir_path="textbook_corpus/").corpus

    # Initialize the Concordancer with the loaded corpus
    c = Concordancer(corpus)


Utility Function for CQL Search
-----------------

Create a function to facilitate Corpus Query Language (CQL) searches and display results:

.. code-block:: python

    def get_first_n(cql, n=10, left=5, right=5):
        out = []
        for i, r in enumerate(c.cql_search(cql, left=left, right=right)):
            if i == n: break
            out.append(r)
        return out


Search by Characters
-----------------
Perform searches based on character-specific criteria.


.. code-block:: python

    cql = """
    [char="窗"] [char="[一-窗]"] 
    """
    results = get_first_n(cql, n=5)
    results

This prints:
 

.. container:: output execute_result

      ::

        [
            <Concord 門、客廳和{窗戶}旁貼上年畫>,
            <Concord 水匠來，把{窗子}用甎頭堵上>,
            <Concord 子，就指著{窗子}說：「這兩>,
            <Concord 大門上、紙{窗旁}，幾乎都貼>,
            <Concord 要把這兩個{窗子}堵起來。」>,
        ]


To examine detailed information about a specific match, retrieve the ``data`` attribute from a Concordance object.

.. code-block:: python

    result_1 = results[0]
    result_1.data

This prints:

.. code-block:: python

    {
        'left': '門、客廳和',
        'keyword': '窗戶',
        'right': '旁貼上年畫',
        'position': (3, 11, 0, 25),
        'meta': {
            'id': '4S/90-1-有趣的年畫.txt',
            'time': {
                'label': '教科書課文 - 4下', 
                'ord': 4, 
                'year': ['90', '88', '69']
            },
            'text': {
                'lesson': '1', 
                'title': '有趣的年畫', 
                'year': '90'
            }
        },
        'captureGroups': {}
    }


Search by Character Components
-----------------
Explore additional character searches using Kangxi radicals and Ideographic Description Characters (IDCs).


-----------------
Kangxi Radical
-----------------

.. code-block:: python

    cql = """
    [radical="穴"]
    """
    get_first_n(cql, 5)


This prints:


.. container:: output execute_result

      ::

        [
            <Concord 更飛進了太{空}。萊特兄弟>,
            <Concord 以後，一有{空}，我就要哥>,
            <Concord 高的掛在天{空}。好多人看>,
            <Concord 笑語，聞著{空}氣中淡淡的>,
            <Concord 箭手，不論{空}中的飛雁，>,
        ]

-----------------
IDC
-----------------

.. code-block:: python

    cql = """
    [compo="木" & idc="horz2"] # 'horz2' represents '⿰'
    """
    get_first_n(cql, 5)


.. container:: output execute_result

      ::

        [
            <Concord 舞動，這個{栩}栩如生的掌>,
            <Concord 動，這個栩{栩}如生的掌中>,
            <Concord 城河上的小{橋}，穿過古老>,
            <Concord 巒溪的長虹{橋}附近，兩岸>,
            <Concord 來到人間的{橋}梁。小弟弟>,
        ]



-----------------
Radical Semantic Type
-----------------

One can also search by the semantic type of Kangxi radicals based on Ma’s (2016) classification.


.. code-block:: python

    cql = '''
    [semtag="植物"] [semtag="植物"]
    '''
    get_first_n(cql, 5)


This prints:
 
.. container:: output execute_result

      ::

        [
            <Concord 握細緻的小{楷筆},一筆一畫>,
            <Concord 年的歷史，{梁柱}雕刻很細緻>,
            <Concord 在二十世紀{萌芽}的新科技，>,
            <Concord 印象深刻。{花蓮}秀姑巒溪的>,
            <Concord 遠到宜蘭、{花蓮}，深入原住>,
        ]



Search by Phonetic Properties
-----------------

Explore phonetic aspects of the text by utilizing specific phonetic attributes available in the corpus.


-----------------
Mandarin
-----------------

.. code-block:: python

    cql = '''
    [phon="ㄨㄥ" & tone="1" & sys="moe"]
    '''
    get_first_n(cql, 5)


This prints: 

.. container:: output execute_result

      ::

        [
            <Concord 前有一個富{翁}，很迷信。>,
            <Concord 起來。」富{翁}聽了，就叫>,
            <Concord 。他就對富{翁}說：「這棵>,
            <Concord 棵樹。」富{翁}聽了，覺得>,
            <Concord 有一天，富{翁}的朋友來，>,
        ]



-----------------
Middle Chinese
-----------------

.. code-block:: python

    cql = '''
    [韻母="東" & 聲調="平" & sys="廣韻"]
    '''
    get_first_n(cql, 5)

This prints: 

.. container:: output execute_result

      ::

        [
            <Concord 我要學給有{蟲}的樹治病，>,
            <Concord ，只剩竹節{蟲}與枯葉蝶，>,
            <Concord 驚嘆。竹節{蟲}與枯葉蝶就>,
            <Concord 眼前，竹節{蟲}和竹子的細>,
            <Concord 比賽，竹節{蟲}與枯葉蝶勝>,
        ]


Setting Up Analysis Tools
-----------------

Initialize the necessary tools for component analysis, concordance searches, and dispersion analysis. This setup enables detailed linguistic exploration within the ``textbook_corpus``.


.. code-block:: python

    from hgct import CompoAnalysis, PlainTextReader, Concordancer, Dispersion

    CA = CompoAnalysis(PlainTextReader("textbook_corpus/", auto_load=False))
    CC = Concordancer(PlainTextReader("textbook_corpus/").corpus)
    DP = Dispersion(PlainTextReader("textbook_corpus/").corpus)


Frequency Distribution Analysis
-----------------

-----------------
Character
-----------------

Retrieve the most common characters from a 5th grade fall textbook. The ``tp`` parameter specifies the type; here it is set to "chr" for characters.

.. code-block:: python

    CA.freq_distr(tp="chr", subcorp_idx=5).most_common(4)

This prints: 

.. code-block:: python

    [('的', 108), ('，', 104), ('。', 68), ('了', 47)]


-----------------
Characters with a given radical
-----------------

Calculate the frequency of characters containing the radical "水" across the same textbook.


.. code-block:: python

    CA.freq_distr(tp=None, radical="水", subcorp_idx=5).most_common(4)


This prints: 

.. code-block:: python

    [('洲', 21), ('海', 19), ('沒', 16), ('湖', 16)]


-----------------
Characters with a given IDC component
-----------------

Analyze the frequency of characters containing the IDC component "土" with a vertical arrangement in the same textbook.


.. code-block:: python

    CA.freq_distr(tp=None, compo="土", idc="vert2", subcorp_idx=5)

This prints:

.. code-block:: python

    Counter({'王': 30,
         '去': 27,
         '走': 10,
         '堅': 5,
         '幸': 5,
         '墓': 5,
         '至': 4,
         '壁': 4,
         '堂': 3,
         '主': 2,
         '基': 2,
         '赤': 1,
         '堡': 1})


Dispersion Analysis
-----------------

Analyze how uniformly certain characters are spread throughout the corpus to understand their usage patterns. In this example, we look at the dispersion of '的' (a function word) and '花' (a content word).


.. code-block:: python

    import pandas as pd

    df_disp = []

    for ch in '的花':
        stats, raw = DP.char_dispersion(
            char=ch, subcorp_idx=0, return_raw=True
        )
        d = {
            'char': ch,
            'Range(%)': '{:.2f}'.format(100 * stats['Range'] / raw['n']),  # Normalize range as a percentage of total segments
            **stats  # Include all other stats
        }
        df_disp.append(d)

    df_disp = pd.DataFrame(df_disp)
    df_disp

This prints: 

.. list-table:: 
   :widths: 25 25 25 25 25 25 25 25
   :header-rows: 1

   * - Char
     - Range(%)
     - Range
     - DP
     - DPnorm
     - KLdivergence
     - JuillandD
     - RosengrenS
   * - 的
     - 100.00
     - 9
     - 0.179573
     - 0.187460
     - 0.126840
     - 0.840689
     - 0.955655
   * - 花
     - 33.33
     - 3
     - 0.686952
     - 0.717124
     - 1.899763
     - 0.384915
     - 0.290457


Ngram and Collocation Analysis
-----------------

Analyze bigrams and their associations using various statistical measures to better understand the common pairings and their strengths in a 5th grade fall textbook corpus.


.. code-block:: python

    # Frequency distribution of 2-gram ngrams
    CC.freq_distr_ngrams(n=2, subcorp_idx=5).most_common(4)

This prints:

.. code-block:: python

    [('他們', 26), ('母親', 26), ('我們', 25), ('一個', 23)]
 

.. code-block:: python

    # Bigram associations sorted by G-squared statistic
    bi_asso = CC.bigram_associations(subcorp_idx=5, sort_by="Gsq")
    bi_asso[0]

This prints:

.. code-block:: python

    (
     '母親',
     {
        'MI': 8.254205080149351,
        'Xsq': 7934.8041752841245,
        'Gsq': 329.2349988448261,
        'Dice': 0.9285714285714286,
        'DeltaP21': 0.9626357378320729,
        'DeltaP12': 0.8964426252943788,
        'FisherExact': 3.6528671910409246e-72,
        'RawCount': 26
     }
    )


.. code-block:: python

    d = pd.DataFrame([{'bigram': x[0], **x[1]} for x in bi_asso][:5])
    d

This prints:
 
.. list-table:: 
   :widths: 25 25 25 25 25 25 25 25 25
   :header-rows: 1

   * - bigram
     - MI
     - Xsq
     - Gsq 
     - Dice
     - DeltaP21
     - DeltaP12
     - FisherExact
     - RawCount
   * - 母親   
     - 8.254205
     - 7934.8042 
     - 329.2350  
     - 0.928571 
     - 0.962636 
     - 0.896443 
     - 3.652867e-72         
     - 26   
   * - 時候
     - 7.674781
     - 3871.3328
     - 211.5859
     - 0.593750
     - 0.422222
     - 0.997167
     - 1.488648e-46
     - 19
   * - 企鵝
     - 9.466194
     - 9195.0000
     - 196.5797
     - 1.000000
     - 1.000000
     - 1.000000
     - 1.869793e-42
     - 13
   * - 南極
     - 8.435315
     - 5531.9219
     - 195.0192
     - 0.761905
     - 0.940196
     - 0.639891
     - 2.816916e-43
     - 16
   * - 小昌
     - 7.235897
     - 2700.5653
     - 186.4523
     - 0.455696
     - 0.295082
     - 0.995314
     - 3.869527e-41
     - 18