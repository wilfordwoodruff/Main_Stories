library(shiny)
library(tidyverse)
library(leaflet)
library(DT)

writings <- read_csv("https://github.com/wilfordwoodruff/Main-Data/raw/main/data/derived/derived_data.csv")

# Define UI for application that draws a histogram
ui <- function(request) {
  fluidPage(
    #EDIT Colors and appearance,
    theme = bslib::bs_theme(bootswatch = "united"),
    
    # Application title
    titlePanel("Explore President Woodruff's Diaries"),
    
    # Remove or add buttons you Want 
    sidebarLayout(
      sidebarPanel(
        checkboxGroupInput(inputId = 'journal_type',
                           label = 'Types of Writings',
                           choices = unique(writings$`Document Type`),
                           selected = unique(writings$`Document Type`)
                           
        ),
        textInput(inputId='word_search',
                  label='Search for a Specific Word',
                  placeholder= "e.g. Utah"),
        bookmarkButton()
      ),
      
    #Where the Output will end up
    mainPanel(
      htmlOutput("explanation"),
      plotOutput("sample_chart")
    )
  )
)}

server <- function(input, output) {
  
  #Collect the values that will update over time
  selections <- reactiveValues()
  observe({
    selections$filtered_writing <- writings %>%
      mutate(`Word Count`=str_count(`Text Only Transcript`,input$word_search)) %>%
      filter(`Word Count` > 0 & `Document Type` %in% input$journal_type)
  })
  output$sample_chart <- renderPlot({
    ggplot(selections$filtered_writing, aes(x=Order,y=`Word Count`)) +
      geom_col()  + theme_gray() +
      labs(y=paste("Number of Times \"",input$word_search, "\" Is Referenced",sep=''),
           title=paste("How Much Does Pres. Woodruff Talk About \"",input$word_search,"\"?",sep=''))
  })
  
  output$explanation <- renderUI({
    HTML("Here's a sample App you can build from. The buttons on the left are customizable, and you can add anyhting here that might let people see Pres. Woodruff's works in a new way.")
  })
}



# Run the application 
shinyApp(ui = ui, server = server,enableBookmarking = "url")

