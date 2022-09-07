new Vue ({ 
    el: "#app",
  
    data() {
        return {
          ticker: "default",
          tickers: [
            { name: "DEMO1", price: "-" },
            { name: "DEMO2", price: "2" },
            { name: "DEMO3", price: "-" }
          ]
        };
      },
  
    methods: {
      add() {
        const newTicker = {
          name: this.ticker,
          price: "-"
        };
  
        this.tickers.push(newTicker);
        this.ticker = "";
      },
  
      handleDelete(tickerToRemove) {
        this.tickers = this.tickers.filter(t => t !== tickerToRemove);
      }
    }
  })