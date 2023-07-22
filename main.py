import streamlit
import matplotlib.pyplot
import numpy
import string
import pandas

streamlit.write('# Entropy of written English')
streamlit.write('Entropy is a measure of the uncertainty or randomness of a system. In the context of written English, entropy can refer to the amount of unpredictability or variability in the language.')

text = streamlit.text_area("Text to analyse")


def Cloud(text):
    from wordcloud import WordCloud
    cloud = WordCloud().generate(text)
    fig = matplotlib.pyplot.figure()
    matplotlib.pyplot.imshow(cloud)
    matplotlib.pyplot.axis('off')
    return fig



def diswl(text):
    words = text.split()
    count = numpy.zeros(40)
    for i in words:
        count[len(i)]+=1
    fig = matplotlib.pyplot.figure()
    matplotlib.pyplot.bar(range(len(count)),count)
    matplotlib.pyplot.xlabel('Length')
    matplotlib.pyplot.ylabel('Frequency')
    return fig

def letter_frequency(text):
    letters = list(text)
    diction = {}
    for i in letters:
        if i in string.ascii_letters:
            i = i.lower()
            diction[str(i)]=diction.get(i,0)
            diction[str(i)]+=1
        else:
            continue
    fig = matplotlib.pyplot.figure()
    pandas.Series(data=diction).sort_index().plot(kind='bar',xlabel='Letter',ylabel='Count')
    return fig

def lf_prob(text):
    letters = list(text)
    diction = {}
    for i in letters:
        if i in string.ascii_letters:
            i = i.lower()
            diction[str(i)]=diction.get(i,0)
            diction[str(i)]+=1
        else:
            continue
    probability = {}
    for i in string.ascii_lowercase:
        try:
            probability[str(i)]=diction[i]/sum(diction.values())
        except:
            pass
    fig = matplotlib.pyplot.figure()
    entrophy = -sum(list(probability.values())*numpy.log2(list(probability.values())))
    pandas.Series(data=probability).sort_index().plot(kind='bar',xlabel='Letter',ylabel='Probability',title='Entropy= %.3f'%entrophy)
    return fig


def cond_entropy(text):
    letters = string.ascii_lowercase
    num_letters = len(string.ascii_lowercase)
    probability_matrix = numpy.zeros([num_letters,num_letters])


    for i in range(len(text)-1):
        currlet = text[i]
        nextlet = text[i+1]
        if currlet in letters and nextlet in letters:
            probability_matrix[letters.index(currlet),letters.index(nextlet)]+=1
    print(probability_matrix)

    fig,ax = matplotlib.pyplot.subplots(1,figsize=(10,10))

    ax.imshow(probability_matrix,vmax=500)
    ax.set_ylabel('Current Letter')
    ax.set_xlabel('Next Letter')
    ax.set_xticks(range(num_letters))
    ax.set_yticks(range(num_letters))
    ax.set_xticklabels(letters)
    ax.set_yticklabels(letters)

    return fig

if streamlit.button('Analyse'):
    col1,col2= streamlit.columns(2)
    col1.metric('Letter Count',len(str(text)))
    col2.metric('Word Count',len((text).split(' ')))
    streamlit.write('## Distribution of Word Length')
    streamlit.pyplot(diswl(text))
    streamlit.write('## Frequency of Letters')
    streamlit.pyplot(letter_frequency(text))
    streamlit.write('## Probability of Frequency')
    streamlit.pyplot(lf_prob(text))
    streamlit.write('## Conditional Frequency')
    streamlit.pyplot(cond_entropy(text))
else:
    pass
