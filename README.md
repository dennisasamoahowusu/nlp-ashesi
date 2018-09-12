# nlp-ashesi
This repository is for projects relating to NLP that I am involved with at Ashesi University. The members of this repository are students whose capstones I am supervising and students involved with SEEL @Ashesi NLP projects.

## Bilingual Turn Preaching
It happens in some churches in Ghana that when the pastor who is preaching in English makes a statement or statements, he pauses for a translator to say what he just said to the audience in the local language. This is what I call Bilingual Turn Preaching. What we are investigating, in this project, is whether, and to what extent, a significant amount of audios from these churches can be useful as a linguistic resource for developing NLP systems in Ghanaian local languages. The value of this exploration lies in the fact that this resource is something we can get in significant amounts quite cheaply and quickly. Thus, if we can show it to be useful as an NLP resource, we would have found a feasible way to get enough data to build NLP systems in Ghanaian languages for, at least, certain tasks. 

Some recent works have looked into translating speech in one language directly to text in another language (Berard et al., 2016), (Duong et al., 2016), (Anastasopoulos et al., 2016). Normally, to translate speech in one language, called the source language, to text in another language, called the target language, the source language is transcribed and then the text is translated into the target language. In cases where you have the data to train a speech recognizer - vasts amount of audio and their transcriptions - this approach is fine. Where this data is not available, as we have in Ghana, we need alternative approaches. We could try to build the data for speech recognition but that will be expensive to do as we will need to collect audios and hire people to transcribe them. In any case, we do not have enough text in the Ghanaian languages to build reliable language models which are also necessary for speech recognition. Thus, the approach of attempting to translate source speech directly into target language text is of interest.

This approach, however, requires its own kind of data, namely, audio in the source language and corresponding text translation in the target language. Where reliable speech recognition models exist for the target language, audio translations could be collected instead of text translations. The translation audios can then be transcribed to get text translations.


