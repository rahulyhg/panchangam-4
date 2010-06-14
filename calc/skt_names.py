#!/usr/bin/python
# -*- coding: utf-8 -*-

ahoratram = 'अहोरात्रम्'
adhika = 'अधिक'
ekadashi = 'एकादशी'

nakshatra_names={1:'अश्विनी',
2:'अपभरणी',
3:'कृत्तिका',
4:'रोहिणी',
5:'मृगशीर्ष',
6:'आर्द्रा',
7:'पुनर्वसू',
8:'पुष्य',
9:'आश्रेषा',
10:'मघा',
11:'पूर्वफल्गुनी',
12:'उत्तरफल्गुनी',
13:'हस्त',
14:'चित्रा',
15:'स्वाति',
16:'विशाखा',
17:'अनूराधा',
18:'ज्येष्ठा',
19:'मूला',
20:'पूर्वाषाढा',
21:'उत्तराषाढा',
22:'श्रवण',
23:'श्रविष्ठा',
24:'शतभिषक्',
25:'पूर्वप्रोष्ठपदा',
26:'उत्तरप्रोष्ठपदा',
27:'रेवती'}

masa_names={1:'मेष',
2:'वृषभ',
3:'मिथुन',
4:'कर्कटक',
5:'सिंह',
6:'कन्या',
7:'तुला',
8:'वृश्चिक',
9:'धनुः',
10:'मकर',
11:'कुम्भ',
12:'मीन'}

chandra_masa_names={1:'चैत्र',
2:'वैशाख',
3:'ज्यैष्ठ',
4:'आषाढ',
5:'श्रवण',
6:'भाद्रपद',
7:'आश्विन',
8:'कार्तिक',
9:'मार्गशीर्ष',
10:'पौष',
11:'माघ',
12:'फाल्गुन'}

tithi_names={1:'शुक्ल~प्रथमा',
2:'शुक्ल~द्वितीया',
3:'शुक्ल~तृतीया',
4:'शुक्ल~चतुर्थी',
5:'शुक्ल~पञ्चमी',
6:'शुक्ल~षष्ठी',
7:'शुक्ल~सप्तमी',
8:'शुक्ल~अष्टमी',
9:'शुक्ल~नवमी',
10:'शुक्ल~दशमी',
11:'शुक्ल~एकादशी',
12:'शुक्ल~द्वादशी',
13:'शुक्ल~त्रयोदशी',
14:'शुक्ल~चतुर्दशी',
15:'\\fullmoon~पूर्णिमा',
16:'कृष्ण~प्रथमा',
17:'कृष्ण~द्वितीया',
18:'कृष्ण~तृतीया',
19:'कृष्ण~चतुर्थी',
20:'कृष्ण~पञ्चमी',
21:'कृष्ण~षष्ठी',
22:'कृष्ण~सप्तमी',
23:'कृष्ण~अष्टमी',
24:'कृष्ण~नवमी',
25:'कृष्ण~दशमी',
26:'कृष्ण~एकादशी',
27:'कृष्ण~द्वादशी',
28:'कृष्ण~त्रयोदशी',
29:'कृष्ण~चतुर्दशी',
30:'\\newmoon~अमावस्या'}

year_names={1:'प्रभव',
2:'विभव',
3:'शुक्ल',
4:'प्रमोद',
5:'प्रजापति',
6:'आङ्गिरस',
7:'श्रीमुख',
8:'भाव',
9:'युव',
10:'धात्री',
11:'ईश्वर',
12:'बहुधान्य',
13:'प्रमाधि',
14:'विक्रम',
15:'वृष',
16:'चित्रभानु',
17:'स्वभानु',
18:'तारण',
19:'पार्थिव',
20:'व्यय',
21:'सर्वजित्',
22:'सर्वधारी',
23:'विरोधी',
24:'विकृति',
25:'खर',
26:'नन्दन',
27:'विजय',
28:'जय',
29:'मन्मथ',
30:'दुर्मुखी',
31:'हेविलम्बी',
32:'विलम्बी',
33:'विकारी',
34:'शार्वरी',
35:'प्लव',
36:'शुभकृत्',
37:'शोभकृत्',
38:'क्रोधी',
39:'विश्वावसु',
40:'पराभव',
41:'प्लवङ्ग',
42:'कीलक',
43:'सौम्य',
44:'साधारण',
45:'विरोधिकृति',
46:'परिधावी',
47:'प्रमादीच',
48:'आनन्द',
49:'राक्षस',
50:'नल',
51:'पिङ्गल',
52:'कलायुक्ति',
53:'सिद्धार्थी',
54:'रौद्र',
55:'दुर्मति',
56:'दुन्दुभि',
57:'रुधिरोद्गारी',
58:'रक्ताक्षी',
59:'क्रोधन',
60:'अक्षय'}

karanam_names={1:'किंस्तुघ्न',
2:'बव',
3:'बालव',
4:'कौलव',
5:'तैतिल',
6:'गर',
7:'वणिज',
8:'विष्टि',
9:'बव',
10:'बालव',
11:'कौलव',
12:'तैतिल',
13:'गर',
14:'वणिज',
15:'विष्टि',
16:'बव',
17:'बालव',
18:'कौलव',
19:'तैतिल',
20:'गर',
21:'वणिज',
22:'विष्टि',
23:'बव',
24:'बालव',
25:'कौलव',
26:'तैतिल',
27:'गर',
28:'वणिज',
29:'विष्टि',
30:'बव',
31:'बालव',
32:'कौलव',
33:'तैतिल',
34:'गर',
35:'वणिज',
36:'विष्टि',
37:'बव',
38:'बालव',
39:'कौलव',
40:'तैतिल',
41:'गर',
42:'वणिज',
43:'विष्टि',
44:'बव',
45:'बालव',
46:'कौलव',
47:'तैतिल',
48:'गर',
49:'वणिज',
50:'विष्टि',
51:'बव',
52:'बालव',
53:'कौलव',
54:'तैतिल',
55:'गर',
56:'वणिज',
57:'विष्टि',
58:'शकुनि',
59:'चतुष्पाद',
60:'नागव'}

yogam_names={1:'विष्कुम्भ',
2:'प्रीति',
3:'आयुष्मान्',
4:'सौभाग्य',
5:'शोभन',
6:'अतिगण्ड',
7:'सुकर्मा',
8:'धृति',
9:'शूल',
10:'गण्ड',
11:'वृद्धि',
12:'ध्रुव',
13:'व्याघात',
14:'हर्षण',
15:'वज्र',
16:'सिद्धि',
17:'व्यतीपात',
18:'वारीयन',
19:'परिघ',
20:'शिव',
21:'सिद्ध',
22:'साध्य',
23:'शुभ',
24:'शुक्ल',
25:'ब्रह्म',
26:'ऐन्द्र',
27:'वैधृति'}

shukla_ekadashi_names={1:'कामद',
2:'मोहिनी',
3:'पाण्डव निर्जल',
4:'पद्म',
5:'पुत्रद/पवित्रोपान',
6:'परिवर्तिनि',
7:'पाशाङ्कुश',
8:'उत्तान',
9:'वैकुण्ठ',
10:'पुत्रद',
11:'जया',
12:'अमलकी',
13:'पद्मिनी'}

krishna_ekadashi_names={1:'पापविमोचिनी',
2:'वरुथिनी',
3:'अपरा',
4:'योगिनी',
5:'कामिक',
6:'अज',
7:'इन्दिरा',
8:'रमा',
9:'उत्पन्न',
10:'सफल',
11:'त्रिस्पृश',
12:'विजया',
13:'परमा'}


