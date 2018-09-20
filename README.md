
# nlp-ashesi
This repository is for projects relating to NLP that I am involved with at Ashesi University. The members of this repository are students whose capstones I am supervising and students involved with SEEL @Ashesi NLP projects.

## Natural Language Processing for Native Ghanaian Languages

It is desirable to develop NLP systems for Ghanaian languages even if the power of those systems are relatively limited. The Farmers Aid project, described below, describes a use case for an NLP system that recognizes and processes speech for a very limited domain. This work explores various approaches to building an NLP system for Ghanaian languages bearing in mind a limited use case like what is described in the Farmers Aid project. We will examine and demonstrate the feasibility or lack thereof of building a system for this task via conventional means (i.e. in a way that is very similar to how such a system might be developed in, say, English). We will explore other approaches that fall into two categories. The first category is the use of unconventional data sources such as Bible and hymnbook translations, bilingual turn preaching (described below) etc. The second category is the use of limited conventional data sources. For instance, we might create a limited amount of audio with their transcriptions. The question we will be attempting to answer is whether any of these approaches or a hodge podge of them could be effective for developing an NLP system for a task as limited in scope as the Farmers Aid project.

**Proposed by:** Dennis Asamoah Owusu

**Main Contributors:** Dennis Asamoah Owusu, David Sasu

## Bilingual Turn Preaching
It happens in some churches in Ghana that when the pastor who is preaching in English makes a statement or statements, he pauses for a translator to say what he just said to the audience in the local language. This is what I call Bilingual Turn Preaching. What we are investigating, in this project, is whether, and to what extent, a significant amount of audios from such churches can be useful as a linguistic resource for developing NLP systems in Ghanaian local languages. The value of this exploration lies in the fact that this resource is something we can get in significant amounts quite cheaply and quickly. Thus, if we can show it to be useful as an NLP resource, we would have found a feasible way to get enough data to build NLP systems in Ghanaian languages for, at least, certain tasks. 

Some recent works have looked into translating speech in one language directly to text in another language (Berard et al., 2016), (Duong et al., 2016), (Anastasopoulos et al., 2016). Normally, to translate speech in one language, called the source language, to text in another language, called the target language, the audio in the source language is transcribed and the transcription is then translated into the target language. In cases where you have the data to train a speech recognizer - vasts amount of audio and their transcriptions - this approach is fine. Where this data is not available, as we have in Ghana, we need alternative approaches. We could try to build the data for speech recognition but that will be expensive to do as we will need to collect audios and hire people to transcribe them. In any case, we do not have enough text in the Ghanaian languages to build reliable language models which are also necessary for speech recognition. Thus, the approach of attempting to translate source speech directly into target language text is of interest.

This approach, however, requires its own kind of data, namely, audio in the source language and corresponding text translation in the target language. Where reliable speech recognition models exist for the target language, audio translations could be collected instead of text translations. The audio translations can then be transcribed to text. We see bilingual turn preaching as a potential source of data for direct speech translation. The data, however, exists in a form that is not ready for speech translation. Each audio in our collection will contain a mixture of English and the Ghanaian language with a statement or set of statements in English being followed by its translation in a local language. 

If we wanted to use the data in the manner that others who have attempted speech translation have, we will have to find a way to segment the data - determine where english utterances begin and end and where local language utterances begin and end. (Perhaps, using language identification?) Then, we will have to pair english statements with local language statements. Beyond this problem of segmentation and pairing, the data has its own perculiarities including the fact that not everything that is said in English may end up in the translation and translators sometimes add things the preacher did not say. Some translations may also just be plain wrong since those translating are not necessarily experts in both languages. Furthermore, the data is likely to have significant noise considering the fact that in some churches, the parishioners clap or shout statements as the preaching is going on. There is also the question of the limitedness of the domain and whether what is learned from the data may be useful in non-church settings.

Despite the perculiarities and challenges of this data source, it may still be possible to extract useful information. The hope stems from the fact that we can potentially collect significant amounts of this sort of data. This implies that we will not be limited in terms of which machine learning algorithms and techniques we can apply. Our goal is to figure out a way to use this data for some nlp system. The contributions of this work will include collecting and open sourcing bilingual turn preachings in Ghanaian languages, providing a systematic way to segment and pair translated statements or pairs of translated statements from the audio, providing a systematic way to learn associations between local language words or phrases and English words and phrases, and demonstrating how the learned associations can be useful in some NLP task. Even though we will be looking at direct speech translation, we will also look at possibly extracting useful information from the audios even without segmentation and pairing.    

**Proposed by:** Dennis Asamoah Owusu

**Main Contributors:** Dennis Asamoah Owusu, David Sasu

## Ashesi Support Bot

The Ashesi Support Center is intended as a one-stop shop for reporting and getting solutions/answers to problems/questions members of the Ashesi community have. In particular, a support center email has been setup to which members of the Ashesi community are encouraged to send any questions or problems. When this email is received, a support center staff looks at the email, determines who is the best person to respond to or solve that problem and then notifies the person to handle the task. As the number of emails increase, it will take a longer time before emails received are routed to the people who can respond to them. The first job of the Ashesi Support bot is to predict who a support email should be sent to. The second job of the support bot is to attempt to automatically answer queries in emails where possible. We will also be looking into a chatbot that can answer queries and guide people to resolve some of the issues for which they contact support.

**Proposed by:** Dennis Asamoah Owusu

**Main Contributors:** Dennis Asamoah Owusu


## One-for-All Support System for Financial Institutions

In some financial institutions, customers are assigned relationship managers that they can contact with their issues for resolution. Customers, typically, have the phone numbers or emails of these relationship managers and email, call or text them with their problems. This direct to direct communication between customers and their relationship managers provides no direct and transparent way for the bank to directly monitor customer issues as well how relationship managers are doing in responding to these customer requests. At the same time, texting is, increasingly, a preffered way for people, especially, young people, to communicate.  There may be some advantages to providing one single point/platform customers should use in reaching their relationship managers. The messages sent can then be routed to the relationship manager associated with the customer. This way provides a way for the bank to directly and transparently monitor customer issues. 

More than that, it provides a way for the bank to take advantage of NLP technologies to improve the customer experience. First, a bot could be used to resolve some of the customer issues. Suppose, customer A makes an enquiry about what is needed to open an additional account and the relationship manager answers that and then the next day customer B asks the same question, perhaps, differently worded. An intelligent bot could recognize that customer B is seeking the same answer as B and automatically respond. Secondly, for certain requests, relationship managers simply relay the request to some appriopriate department to handle. An intelligent bot could do that as well. For instance, it could route a card related request to the cards department as soon as the message is received and then alert the relationship manager that this request came in and the message has been relayed to the cards department. This will avoid the delay between when a request comes in and when a relationship manager is able to read the request and then relay it. It will also save the relationship manager time as (s)he does not have to relay the request. Many more advantages can be presented but these two should suffice to show the relevance of this project.

This project will seek to crowdsource and opensource a dataset for building such a financial system. We will attempt to get customers of financial institutions to share some of the issues they contact or will like to contact their relationship managers or customer support about. Since talking is probably an easier way for customers to respond, we should make it possible for them to share this information through speech if they so choose. In building this dataset, speech and language technologies will be applied for efficiency and, thus, widening the scope of the project. To further widen the scope of the project, we could consider the one-for-all support system as being not only for current customers of the financial institution but for potential clients who want to, say, find about what it takes to open an account with the bank.

**Proposed by:** Dennis Asamoah Owusu

**Main Contributors:** Dennis Asamoah Owusu


## Ok Nsesa!

This work will explore the use of voice interface in the selling of food at Ashesi University. One of the problems that food sellers and buyers face at Ashesi is the difficulty of getting change for buyers especially when the change amount is small like 20 pesewas, 40 pesewas etc. One way that this is handled currently is for sellers to either keep the change or simply tell buyers to come for their change later. Sometimes, the sellers write the change amount and the day's date on a receipt; the idea being that buyers can bring the receipt later for their change or use the change as part payment for their next purchase. On occasion, sellers don't collect the full amount to avoid needing to give change. For instance, the seller may let the buyer pay 1 cedi for an item that costs 1.20 cedis to avoid needing to give change.

The current situation is not satisfactory. Some buyers complain of losing change. This happens because a buyer may forget to collect their change or misplace the receipt that has the change amount by their next purchase. Sellers should care about this because it negatively impacts the customer experience. Sometimes, valuable time is wasted disputing about change. This situation may be ripe for some technological intervention. The basic idea is for buyer's change to be converted to electronic money which they can use for buying mobile phone credit or donating to some cause at Ashesi or for some other electronic purchase. Also, they should be able to use their electronic change to purchase food from the vendor if they accumulate enough. This process of converting change to electronic money during a purchase must be fast enough to be worth it. Sellers and buyers alike may be loath to waste precious time on 20 or 50 pesewas change. 

A voice interface may provide a quick way for sellers to give electronic change. At a point that the seller realizes that (s)he does not have change to give the buyer, the buyer, for instance, "Collect 50 pesewas" and their electronic account gets credited. This, we assume, will be faster and more convenient than having to navigate a graphical user interface to perform the same task. Part of the speed and convenience of voice interfaces lies in the fact that voice instructions can simultaneously be used for identity determination and authorization. The first part of this project is building a system that will allow sellers to give buyers electronic change through a voice interface. Aside helping to resolve the change issue, nsesa could actually serve as some kind of piggy bank. 

The second part of this project is measuring whether, and to what extent, a voice interface can improve turnaround when it comes to buying and selling food. It is common to see queues at food vendor points. Graphical user interfaces are used by the sellers to check if users have enough money on their cards and to input into the system what the user is buying. Might turnaround time be improved if a voice interface was used in lieu of the graphical interface and, if it will, to what extent? Dealing with change is itself a time waster. Could we do better if people paid through voice? This project will involve developing an alternative system to buying and selling food in which voice interfaces are the main means of interaction. Once that is done, we will perform controlled experiments to measure improvements/deterioration in turnaround time.

**Proposed by:** Dennis Asamoah Owusu

**Main Contributors:** Dennis Asamoah Owusu


## Farmers Aid

Providing farmers with information such as the market prices of their goods or what the weather will look like the coming week is beneficial to them. Illiteracy, however, limits the power of systems that are designed for providing farmers information. The author's friend who helped design one such system for farmers and performed user experience research shared that they had to whittle down the system. They shared less information with the farmers because too much information confused them as they could not read. Furthermore, the system could not be interactive - information was just pushed to the farmers. While these farmers could not read or speak English, they have local languages that they are fluent in. What if the farmers could interact with the system in their native language? They could request what information they needed and receive audio responses. 

Another related problem occurs in the profiling of farmers. The farmers are unable to fill a form accurately and thus service providers have to resort to the farmers calling and a person taking down their details. This is not tenable when the number of farmers grows (cite here). Again, what if the farmers could interact with a system that is in their language so they could provide their details without speaking to someone? This project involves prototyping a system that farmers can interact with in their local language to obtain and share information.  

**Proposed by:** Dennis Asamoah Owusu

**Main Contributors:** Dennis Asamoah Owusu


## Emotional State from Pidgin

This project will look at predicting emotional state from pidgin. (Details coming soon)

**Proposed by:** Ekab-Osowo Tawo

**Main Contributors:** Ekab-Osowo Tawo


