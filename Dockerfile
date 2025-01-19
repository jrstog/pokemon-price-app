#Use Python Parent Image
FROM python:3.8-slim

#Set Working Directory
WORKDIR /app

#Copy Contents into Container
COPY . /app

#Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Make Port Available Outside Container for API
EXPOSE 5000

#Define Environment Variable
ENV NAME PokemonPriceApp

#Run Python Script On Container Start
CMD ["python", "app.py"]