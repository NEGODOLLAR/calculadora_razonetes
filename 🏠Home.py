import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os



st.set_page_config(
    page_title="Help MEi",
    layout="centered",
    page_icon="logo.png",
    menu_items={}
)

# Função para criar sidebar personalizado

with st.sidebar:
        # Espaço vazio para empurrar o logo para baixo
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("---")
        st.markdown(
        """
        <span style='color: #FFFFFF; font-weight: bold;'>Help MEI</span><br>
        <span style='color: #FF5F15; font-style: italic;'>Visualize hoje. Cresça amanhã.</span>
        """, 
        unsafe_allow_html=True
    )

# Partículas de fundo
particles_background = """
<style>
    #particles-js {
        position: fixed;
        width: 100%;
        height: 100%;
        z-index: -1;
        top: 0;
        left: 0;
    }
</style>
<div id="particles-js"></div>
<script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
<script>
particlesJS("particles-js", {
    "particles": {
        "number": {
            "value": 80,
            "density": {
                "enable": true,
                "value_area": 800
            }
        },
        "color": {
            "value": "#ffffff"
        },
        "shape": {
            "type": "circle"
        },
        "opacity": {
            "value": 0.5,
            "random": false
        },
        "size": {
            "value": 3,
            "random": true
        },
        "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 1,
            "width": 1
        },
        "move": {
            "enable": true,
            "speed": 1,
            "direction": "none",
            "out_mode": "out"
        }
    },
    "interactivity": {
        "events": {
            "onhover": {
                "enable": true,
                "mode": "repulse"
            },
            "onclick": {
                "enable": true,
                "mode": "push"
            }
        },
        "modes": {
            "repulse": {
                "distance": 100
            },
            "push": {
                "particles_nb": 4
            }
        }
    },
    "retina_detect": true
});
</script>
"""

components.html(particles_background, height=150, width=2000, scrolling=False)

# Conteúdo principal (mantive seu conteúdo original)
st.markdown("""
# 👋 Bem-vindo ao **Painel MEI**

Seja bem-vindo ao **Painel MEI** — uma plataforma interativa criada para ajudar **microempreendedores** a tomarem decisões mais **informadas, seguras e estratégicas** no dia a dia.

Você não está sozinho: muitos MEIs enfrentam desafios na gestão financeira por falta de organização contábil e dificuldade em acessar dados econômicos de forma clara. As informações até existem, mas estão espalhadas e são complexas de interpretar.

É por isso que criamos o **Help MEI**: uma solução prática, visual e poderosa — feita sob medida para o seu negócio.

---

### 💼 Aqui, você encontra:

✅ **Indicadores Econômicos Atualizados**  
✅ **Calculadora Contábil Inteligente**  
✅ **Visual Dinâmico e Intuitivo**  
✅ **Análises que fazem sentido para o seu dia a dia**  

---

### 🚀 Comece agora mesmo!
</div>
""", unsafe_allow_html=True)

# Links para outras páginas
st.page_link("pages/01_📊Painel.py", label="📊 Painel Econômico Interativo para MEI")
st.page_link("pages/02_🧮Calculadora_Contabil.py", label="🧮 Calculadora Contábil")
st.page_link("pages/03_✉️Contatos.py", label="✉️ Contatos")

# Rodapé no final da página
st.markdown("""
<style>
    .footer {
        text-align: center;
        padding: 10px;
        margin-top: 50px;
    }
</style>
<div class="footer">
    <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
        <img alt="Licença Creative Commons" style="border-width:0" 
             src="https://i.creativecommons.org/l/by/4.0/88x31.png" />
    </a>
    <br />
    Este trabalho está licenciado sob uma 
    <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
        Licença Creative Commons Atribuição 4.0 Internacional
    </a>.
</div>
""", unsafe_allow_html=True)