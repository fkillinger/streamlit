from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

img_kc_form = Image.open("images/kc_Feder_logo.jpg")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/6935cd6a-56c4-4940-ad23-8ad9dd84ab0b/p6aKR2nqhu.json")   # Brief

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/33e14c93-4f6e-446d-8417-ed82b79e82fe/ykkTfkPb9S.json")   # bg transparent

# ---- Header section -----
with st.container():
    #st.subheader("Meine neue Webseite")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("#")
        st.subheader("Killinger Engineering")
    with right_column:
        st_lottie(lottie_coding, height=120, key="coding")

st.title("Datenschutz")

with st.container():
    st.write("---")
    # st.write("Angaben gemäß § 5 TMG")
    st.write("##")
    text_column, image_column = st.columns([4,1])

    with text_column:
        st.subheader("Unsere Datenschutzerklärung:")
        st.write("##")
        st.write(
            """
Verantwortlicher im Sinne der Datenschutzgesetze, insbesondere der EU-Datenschutzgrundverordnung (DSGVO), ist:
Killinger Engineering

Unter den angegebenen Kontaktdaten unseres Datenschutzbeauftragten können Sie jederzeit folgende Rechte ausüben:

– Auskunft über Ihre bei uns gespeicherten Daten und deren Verarbeitung (Art. 15 DSGVO),
– Berichtigung unrichtiger personenbezogener Daten (Art. 16 DSGVO),
– Löschung Ihrer bei uns gespeicherten Daten (Art. 17 DSGVO),
– Einschränkung der Datenverarbeitung, sofern wir Ihre Daten aufgrund gesetzlicher Pflichten noch nicht löschen dürfen (Art. 18 DSGVO),
– Widerspruch gegen die Verarbeitung Ihrer Daten bei uns (Art. 21 DSGVO) und
– Datenübertragbarkeit, sofern Sie in die Datenverarbeitung eingewilligt haben oder einen Vertrag mit uns abgeschlossen haben (Art. 20 DSGVO).

Sofern Sie uns eine Einwilligung erteilt haben, können Sie diese jederzeit mit Wirkung für die Zukunft widerrufen.

Sie können sich jederzeit mit einer Beschwerde an eine Aufsichtsbehörde wenden, z. B. an die zuständige Aufsichtsbehörde des Bundeslands Ihres Wohnsitzes oder an die für uns als verantwortliche Stelle zuständige Behörde.
Kontaktformular
Art und Zweck der Verarbeitung:
Die von Ihnen eingegebenen Daten werden zum Zweck der individuellen Kommunikation mit Ihnen gespeichert. Hierfür ist die Angabe einer validen E-Mail-Adresse sowie Ihres Namens erforderlich. Diese dient der Zuordnung der Anfrage und der anschließenden Beantwortung derselben. Die Angabe weiterer Daten ist optional.
Rechtsgrundlage:
Die Verarbeitung der in das Kontaktformular eingegebenen Daten erfolgt auf der Grundlage eines berechtigten Interesses (Art. 6 Abs. 1 lit. f DSGVO).

Durch Bereitstellung des Kontaktformulars möchten wir Ihnen eine unkomplizierte Kontaktaufnahme ermöglichen. Ihre gemachten Angaben werden zum Zwecke der Bearbeitung der Anfrage sowie für mögliche Anschlussfragen gespeichert.

Sofern Sie mit uns Kontakt aufnehmen, um ein Angebot zu erfragen, erfolgt die Verarbeitung der in das Kontaktformular eingegebenen Daten zur Durchführung vorvertraglicher Maßnahmen (Art. 6 Abs. 1 lit. b DSGVO).
Empfänger:
Empfänger der Daten sind ggf. Auftragsverarbeiter.
Speicherdauer:
Daten werden spätestens 6 Monate nach Bearbeitung der Anfrage gelöscht.

Sofern es zu einem Vertragsverhältnis kommt, unterliegen wir den gesetzlichen Aufbewahrungsfristen nach HGB und löschen Ihre Daten nach Ablauf dieser Fristen.
Bereitstellung vorgeschrieben oder erforderlich:
Die Bereitstellung Ihrer personenbezogenen Daten erfolgt freiwillig. Wir können Ihre Anfrage jedoch nur bearbeiten, sofern Sie uns Ihren Namen, Ihre E-Mail-Adresse und den Grund der Anfrage mitteilen.
Verwendung von Cookies
Unsere Richtlinie im Bezug auf Cookies können Sie auf der hier verlinkten Webseite nachlesen.
Information über Ihr Widerspruchsrecht nach Art. 21 DSGVO
Einzelfallbezogenes Widerspruchsrecht

Sie haben das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit gegen die Verarbeitung Sie betreffender personenbezogener Daten, die aufgrund Art. 6 Abs. 1 lit. f DSGVO (Datenverarbeitung auf der Grundlage einer Interessenabwägung) erfolgt, Widerspruch einzulegen; dies gilt auch für ein auf diese Bestimmung gestütztes Profiling im Sinne von Art. 4 Nr. 4 DSGVO.

Legen Sie Widerspruch ein, werden wir Ihre personenbezogenen Daten nicht mehr verarbeiten, es sei denn, wir können zwingende schutzwürdige Gründe für die Verarbeitung nachweisen, die Ihre Interessen, Rechte und Freiheiten überwiegen, oder die Verarbeitung dient der Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen.
Rechte des Nutzers
Sie haben als Nutzer das Recht, auf Antrag eine kostenlose Auskunft darüber zu erhalten, welche personenbezogenen Daten über Sie gespeichert wurden. Sie haben außerdem das Recht auf Berichtigung falscher Daten und auf die Verarbeitungseinschränkung oder Löschung Ihrer personenbezogenen Daten. Falls zutreffend, können Sie auch Ihr Recht auf Datenportabilität geltend machen. Sollten Sie annehmen, dass Ihre Daten unrechtmäßig verarbeitet wurden, können Sie eine Beschwerde bei der zuständigen Aufsichtsbehörde einreichen.
Änderung unserer Datenschutzbestimmungen
Wir behalten uns vor, diese Datenschutzerklärung anzupassen, damit sie stets den aktuellen rechtlichen Anforderungen entspricht oder um Änderungen unserer Leistungen in der Datenschutzerklärung umzusetzen, z.B. bei der Einführung neuer Services. Für Ihren erneuten Besuch gilt dann die neue Datenschutzerklärung.
Fragen an den Datenschutzbeauftragten
Wenn Sie Fragen zum Datenschutz haben, schreiben Sie uns bitte an folgende E-Mail-Adresse: [fritz.killinger@gmail.com]
  
            """, unsafe_allow_html=True
        )

    with image_column:
        st.image(img_kc_form)