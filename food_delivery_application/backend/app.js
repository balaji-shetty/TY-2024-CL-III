// import express from "express";
// import dotenv from "dotenv";
// import cors from "cors";
// import { errorMiddleware } from "./middlewares/error.js";
// import reservationRouter from "./routes/reservationRoute.js";
// import { dbConnection } from "./database/dbConnection.js";

// const app = express();
// dotenv.config({ path: "./config.env" });

// app.use(
//   cors({
//     origin: [process.env.FRONTEND_URL],
//     methods: ["POST"],
//     credentials: true,
//   })
// );
// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

// app.use("/api/v1/reservation", reservationRouter);
// app.get("/", (req, res, next)=>{return res.status(200).json({
//   success: true,
//   message: "HELLO WORLD AGAIN"
// })})

// dbConnection();

// app.use(errorMiddleware);

// export default app;
import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import { errorMiddleware } from "./middlewares/error.js";
import reservationRouter from "./routes/reservationRoute.js";
import { dbConnection } from "./database/dbConnection.js";

const app = express();

// Load environment variables
dotenv.config({ path: "./config.env" });

// Connect to MongoDB
dbConnection();

// CORS setup (allow frontend to access backend)
app.use(
  cors({
    origin: process.env.FRONTEND_URL, // e.g., http://localhost:3000
    methods: ["GET", "POST", "PUT", "DELETE"],
    credentials: true,
  })
);

// Body parsers
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use("/api/v1/reservation", reservationRouter);

app.get("/", (req, res) => {
  return res.status(200).json({
    success: true,
    message: "HELLO WORLD AGAIN",
  });
});

// Global error middleware
app.use(errorMiddleware);

export default app;
