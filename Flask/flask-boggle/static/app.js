
class BoggleRound {
    // New Game

    constructor(game, seconds = 60) {
        this.game = $("#"+ game);

        this.word_list = new Set();
        this.score = 0

        this.seconds = seconds
        this.timer = setInterval(this.oneSecond.bind(this), 1000);

        $(".word-form", this.game).on("submit", this.submitWord.bind(this));
    }

    // Handling messages display
    displayMessage(message) {
        $(".message", this.game)
            .text(message)
    }

    // Displays score
    displayScore() {
        $(".score", this.game).text(`Score: ${this.score}`)
    }

    // "Counts" down seconds
    async oneSecond() {
        this.seconds --;
        $(".time", this.game).text(this.seconds);

        if (this.seconds === 0) {
            $('.word-form').hide()
            clearInterval(this.timer);
            this.displayMessage("Game over!")
            await this.storeScore();
        }
    }

    // Handling submitting words / validating words with server
    async submitWord(e) {
        e.preventDefault();
        const $word = $(".word", this.game);

        // Gets word text / confirms if any input
        let word = $word.val();
        if (word.length === 0) return;

        if (this.word_list.has(word)) {
            this.displayMessage(`You already guessed ${word}!`);
            $word.val("");
            return
        }

        // server validation stuff
        const response = await axios.get("/words", { params: { word: word }});
        if (response.data.result === "not-word") {
            this.displayMessage(`${word} is not a word in our dictionary.`);
        }
        else if (response.data.result === "not-on-board") {
            this.displayMessage(`${word} is not on current board.`);
        }
        else {
            this.displayMessage(`${word} was added!`)
            this.word_list.add(word)
            this.score += word.length
            this.displayScore(this.score)
        }

        // Clear input form
        $word.val("")
    }

    // Sends score to server / notifys if record
    async storeScore() {
        $(".word", this.game).hide()
        const response = await axios.post("/store-score", { score: this.score });
        if (response.data.newRecord) {
            this.displayMessage(`You beat the record! New Record: ${this.score}`)
        } else {
            this.displayMessage(`Nice try! You didn't beat the high score.`)
        }
    }
    
}