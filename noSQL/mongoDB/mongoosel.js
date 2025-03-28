const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/nodeCreatedDB")
const User = mongoose.model("Users",{
    name: String,
    email: String,
    password: String
});

const user = new User({
    name: "Raghav",
    email: "r@r.com",
    password: "123"
})
user.save();