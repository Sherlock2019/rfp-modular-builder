init:
	@echo "Initializing RFP Builder..."
	chmod +x assemble_rfp.sh

build:
	./assemble_rfp.sh

clean:
	rm -f Final_RFP_*.txt

all: init build
gui:
	streamlit run streamlit_app.py
