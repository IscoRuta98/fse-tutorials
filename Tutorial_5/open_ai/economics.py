from agents import Agent, Runner
import asyncio

# Define a Keynesian economist agent.
# Keynesians prioritize government spending to stimulate GDP,
# while noting that monetary policy adjustments are slow in taking effect.
keynesian_agent = Agent(
    name="Keynesian Agent",
    instructions=(
        "You are a Keynesian economist. You believe that increasing government spending "
        "is crucial for stimulating economic growth. While you acknowledge that controlling "
        "the money supply has some impact on GDP, you argue that monetary adjustments take "
        "too long to be effective. Focus on policies that drive government intervention."
    ),
)

# Define a Monetarist economist agent.
# Monetarists focus on controlling the money supply to manage inflation and ensure stability.
monetarist_agent = Agent(
    name="Monetarist Agent",
    instructions=(
        "You are a Monetarist economist. You believe that controlling the money supply is the "
        "most effective way to fight inflation and stabilize the economy. Your policy recommendations "
        "center on adjusting monetary parameters to maintain steady inflation levels, rather than "
        "relying heavily on government spending."
    ),
)

async def main():
    # Prompt the user for a question
    user_question = input("Enter your economics question: ")
    
    # Query both agents with the user-provided question.
    keynesian_result = await Runner.run(keynesian_agent, input=user_question)
    monetarist_result = await Runner.run(monetarist_agent, input=user_question)
    
    # Display the responses from each agent.
    print("\n=== Keynesian Agent Output ===")
    print(keynesian_result.final_output)
    
    print("\n=== Monetarist Agent Output ===")
    print(monetarist_result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
